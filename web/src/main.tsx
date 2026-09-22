import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router";

import { TooltipProvider } from "@/components/ui/tooltip";
import { applyTheme, storedTheme } from "@/theme";

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

// Before the first paint, so the page never flashes the wrong ground.
applyTheme(storedTheme());

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
