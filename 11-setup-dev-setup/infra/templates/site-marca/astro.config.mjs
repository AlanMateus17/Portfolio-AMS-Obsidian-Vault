// Site gerado pelo dev-setup (tools/sites/novo_site.py). Os textos vêm de src/marca.json: edite lá, não nas páginas.
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import marca from "./src/marca.json" with { type: "json" };

export default defineConfig({
  site: marca.dominio ? `https://${marca.dominio}` : "https://example.com",
  integrations: [sitemap()],
});
