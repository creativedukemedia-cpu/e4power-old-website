import fs from "fs";
import os from "os";
import path from "path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { bustKnownEntryScripts, resolveHtmlEntry } from "./_core/vite";
import { issueCmsSession, verifyCmsSession } from "./cmsAuth";

describe("cmsAuth", () => {
  const originalSecret = process.env.JWT_SECRET;

  beforeAll(() => {
    process.env.JWT_SECRET = "test-secret-for-cms-auth";
  });

  afterAll(() => {
    process.env.JWT_SECRET = originalSecret;
  });

  it("issues and verifies a CMS session token", async () => {
    const token = await issueCmsSession({
      sub: "42",
      email: "admin@example.com",
      role: "admin",
      name: "Admin User",
    });

    const payload = await verifyCmsSession(token);

    expect(payload.sub).toBe("42");
    expect(payload.email).toBe("admin@example.com");
    expect(payload.role).toBe("admin");
    expect(payload.name).toBe("Admin User");
  });
});

describe("vite multi-page html resolution", () => {
  let tempRoot = "";

  beforeAll(() => {
    tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "e4-cms-html-"));
    fs.mkdirSync(path.join(tempRoot, "admin"), { recursive: true });
    fs.writeFileSync(path.join(tempRoot, "index.html"), "<html>home</html>");
    fs.writeFileSync(path.join(tempRoot, "admin", "index.html"), "<html>admin</html>");
  });

  afterAll(() => {
    fs.rmSync(tempRoot, { recursive: true, force: true });
  });

  it("resolves nested html entries when they exist", () => {
    const resolved = resolveHtmlEntry(tempRoot, "/admin/index.html");
    expect(resolved).toBe(path.join(tempRoot, "admin", "index.html"));
  });

  it("falls back to the root index when a nested entry does not exist", () => {
    const resolved = resolveHtmlEntry(tempRoot, "/missing/");
    expect(resolved).toBe(path.join(tempRoot, "index.html"));
  });

  it("adds cache-busting params to both known entry scripts", () => {
    const transformed = bustKnownEntryScripts(
      '<script type="module" src="/src/main.tsx"></script><script type="module" src="/src/admin/main.tsx"></script>'
    );

    expect(transformed).toContain('/src/main.tsx?v=');
    expect(transformed).toContain('/src/admin/main.tsx?v=');
  });
});
