import fs from "fs";
import path from "path";
import { describe, expect, it } from "vitest";

const homepagePath = path.resolve(import.meta.dirname, "..", "index.html");
const homepage = fs.readFileSync(homepagePath, "utf8");

describe("homepage theme toggle markup", () => {
  it("keeps a desktop theme toggle and adds a mobile menu toggle", () => {
    expect(homepage).toContain('id="theme-toggle-button"');
    expect(homepage).toContain('id="mobile-theme-toggle-button"');
    expect(homepage).toContain('class="theme-toggle-button mobile-theme-toggle"');
  });

  it("includes the final light-theme patch for lower section readability", () => {
    expect(homepage).toContain('id="theme-light-final-patch"');
    expect(homepage).toContain('body.home-service-menu.theme-light .main-content-block:not(.transparent)');
    expect(homepage).toContain('body.home-service-menu.theme-light .section.dark-gray');
  });

  it("syncs both theme toggle buttons through the shared theme script", () => {
    expect(homepage).toContain("document.getElementById('theme-toggle-button')");
    expect(homepage).toContain("document.getElementById('mobile-theme-toggle-button')");
    expect(homepage).toContain("buttons.forEach(function(button){button.addEventListener('click'");
  });
});
