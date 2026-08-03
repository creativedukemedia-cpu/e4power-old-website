import type { Express } from "express";
import express from "express";
import fs from "fs";
import { type Server } from "http";
import { nanoid } from "nanoid";
import path from "path";
import { createServer as createViteServer } from "vite";
import viteConfig from "../../vite.config";

const CLIENT_ROOT = path.resolve(import.meta.dirname, "../..", "client");
const DIST_ROOT = path.resolve(import.meta.dirname, "../..", "dist", "public");

export function resolveHtmlEntry(rootDir: string, rawUrl: string) {
  const pathname = decodeURIComponent(rawUrl.split("?")[0] || "/");
  const normalized = pathname.startsWith("/") ? pathname.slice(1) : pathname;

  const candidates = [
    normalized,
    normalized ? path.join(normalized, "index.html") : "index.html",
    "index.html",
  ].filter(Boolean);

  for (const candidate of candidates) {
    const fullPath = path.resolve(rootDir, candidate);
    if (!fullPath.startsWith(rootDir)) continue;
    if (fs.existsSync(fullPath) && fs.statSync(fullPath).isFile()) {
      return fullPath;
    }
  }

  return path.resolve(rootDir, "index.html");
}

export function bustKnownEntryScripts(template: string) {
  return template
    .replace(`src="/src/main.tsx"`, `src="/src/main.tsx?v=${nanoid()}"`)
    .replace(`src="/src/admin/main.tsx"`, `src="/src/admin/main.tsx?v=${nanoid()}"`)
    .replace(`src="/src/content/main.tsx"`, `src="/src/content/main.tsx?v=${nanoid()}"`);
}

export async function setupVite(app: Express, server: Server) {
  const serverOptions = {
    middlewareMode: true,
    hmr: { server },
    allowedHosts: true as const,
  };

  const vite = await createViteServer({
    ...viteConfig,
    configFile: false,
    server: serverOptions,
    appType: "custom",
  });

  app.use(vite.middlewares);
  app.use("*", async (req, res, next) => {
    const url = req.originalUrl;

    try {
      const templatePath = resolveHtmlEntry(CLIENT_ROOT, url);
      let template = await fs.promises.readFile(templatePath, "utf-8");
      template = bustKnownEntryScripts(template);
      const page = await vite.transformIndexHtml(url, template);
      res.status(200).set({ "Content-Type": "text/html" }).end(page);
    } catch (e) {
      vite.ssrFixStacktrace(e as Error);
      next(e);
    }
  });
}

export function serveStatic(app: Express) {
  const distPath =
    process.env.NODE_ENV === "development"
      ? DIST_ROOT
      : path.resolve(import.meta.dirname, "public");

  if (!fs.existsSync(distPath)) {
    console.error(
      `Could not find the build directory: ${distPath}, make sure to build the client first`
    );
  }

  app.use(express.static(distPath));

  app.use("*", (req, res) => {
    const entry = resolveHtmlEntry(distPath, req.originalUrl);
    res.sendFile(entry);
  });
}
