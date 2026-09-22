import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router";

import App from "@/App";
import "@/index.css";

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      { index: true, lazy: () => import("@/routes/inbox") },
      { path: "pulls", lazy: () => import("@/routes/inbox") },
      { path: "bots", lazy: () => import("@/routes/inbox") },
    ],
  },
]);

const root = document.getElementById("root");
if (!root) throw new Error("index.html has no #root");

createRoot(root).render(
  <StrictMode>
    <QueryClientProvider client={new QueryClient()}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </StrictMode>,
);
