(ns djclojure.hello.views
  (:require django.shortcuts))

(defn home [request]
  (django.shortcuts/render_to_response "home.html", {}))
