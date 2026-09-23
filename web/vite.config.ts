import path from "node:path";

import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { "@": path.resolve(import.meta.dirname, "./src") },
  },
  server: {
    // The Python API. Only /api is proxied, so the SPA owns every other path.
    proxy: { "/api": "http://127.0.0.1:8000" },
  },
});
