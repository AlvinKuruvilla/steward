import path from "node:path";

import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { "@": path.resolve(import.meta.dirname, "./src") },
  },
  // `tauri dev` loads the interface from here. The port is fixed because
  // src-tauri/tauri.conf.json names it and the API's CORS list allows it.
  server: {
    port: 5173,
    strictPort: true,
  },
  // Vite would clear Rust's compiler output off the terminal it shares.
  clearScreen: false,
});
