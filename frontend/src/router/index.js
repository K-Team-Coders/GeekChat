import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "allservices",

    component: () => import("../views/MainPage.vue"),
  },
  {
    path: "/translater",
    name: "TranslateService",

    component: () => import("../views/TranslatedService.vue"),
  },
  {
    path: "/audio_recognition",
    name: "AudioRecognitionService",

    component: () => import("../views/AudioRecognitionService.vue"),
  },
  {
    path: "/text_to_audio",
    name: "TextToAudioService",

    component: () => import("../views/TextToAudio.vue"),
  },
  {
    path: "/scan_from_docs",
    name: "ScanningDocs",

    component: () => import("../views/DocumentsScan.vue"),
  },
  {
    path: "/search_document",
    name: "SeacrhDocs",
    props(route) {
      return {  text: route.query.text }},

    component: () => import("../views/SearchDocument.vue"),
  },
  {
    path: "/image_recognition",
    name: "ImageRecognition",

    component: () => import("../views/ImageRecognition.vue"),
  },
  {
    path: "/assistant",
    name: "Assistant",

    component: () => import("../views/Assistant.vue"),
  },
  {
    path: "/docs",
    name: "Swagger",

    component: () => import("../views/Docs.vue"),
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: () => import("../components/PageNotFound.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
