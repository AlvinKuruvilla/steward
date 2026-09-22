import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router";

import { TooltipProvider } from "@/components/ui/tooltip";

import App from "@/App";
import "@/index.css";

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      { index: true, lazy: () => import("@/routes/inbox") },
      { path: ":owner/:name", lazy: () => import("@/routes/inbox") },
      {
        path: ":owner/:name/pulls/:number",
        lazy: () => import("@/routes/pull-request"),
      },
    ],
  },
]);

// The system's preference decides the first paint; the attribute is what the
// stylesheet reads, so a toggle can override it later without a reload.
document.documentElement.dataset.theme = window.matchMedia(
  "(prefers-color-scheme: dark)",
).matches
  ? "dark"
  : "light";

const root = document.getElementById("root");
if (!root) throw new Error("index.html has no #root");

createRoot(root).render(
  <StrictMode>
    <QueryClientProvider client={new QueryClient()}>
      <TooltipProvider>
        <RouterProvider router={router} />
      </TooltipProvider>
    </QueryClientProvider>
  </StrictMode>,
);
