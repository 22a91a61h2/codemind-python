<!DOCTYPE html>
<!-- saved from url=(0093)https://owlcoder.technicalhub.io/level-compiler/level-compiler-dark/64e07eb32ceb8b0f3d28e8aa/ -->
<html lang="en" style=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta name="viewport" content="width=device-width"><title>OwlCoder</title><link rel="icon" href="https://owlcoder.technicalhub.io/img/favicon.ico"><link rel="stylesheet" href="./Sum of an Array in Given Range_files/dark.css"><meta name="next-head-count" content="5"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="keywords" content="HTML5 Template Vie onepage themeforest"><meta name="description" content="Vie - Onepage Multi-Purpose HTML5 Template"><meta name="author" content=""><link rel="shortcut icon" href="https://owlcoder.technicalhub.io/img/favicon.ico"><link rel="stylesheet" href="./Sum of an Array in Given Range_files/animate.min.css"><link href="./Sum of an Array in Given Range_files/css" rel="stylesheet"><link href="./Sum of an Array in Given Range_files/css2" rel="stylesheet"><link rel="stylesheet" data-name="vs/editor/editor.main" href="./Sum of an Array in Given Range_files/editor.main.min.css"><link rel="stylesheet" href="./Sum of an Array in Given Range_files/animate.min.css"><link href="./Sum of an Array in Given Range_files/icon" rel="stylesheet"><noscript data-n-css=""></noscript><script defer="" nomodule="" src="./Sum of an Array in Given Range_files/polyfills.js.download"></script><script id="pace" src="./Sum of an Array in Given Range_files/pace.min.js.download" defer="" data-nscript="beforeInteractive"></script><script id="splitting" src="./Sum of an Array in Given Range_files/splitting.min.js.download" defer="" data-nscript="beforeInteractive"></script><script id="isotope" src="./Sum of an Array in Given Range_files/isotope.pkgd.min.js.download" defer="" data-nscript="beforeInteractive"></script><script src="./Sum of an Array in Given Range_files/webpack.js.download" defer=""></script><script src="./Sum of an Array in Given Range_files/main.js.download" defer=""></script><script src="./Sum of an Array in Given Range_files/_app.js.download" defer=""></script><script src="./Sum of an Array in Given Range_files/login-dark.js.download" defer=""></script><script src="./Sum of an Array in Given Range_files/_buildManifest.js.download" defer=""></script><script src="./Sum of an Array in Given Range_files/_ssgManifest.js.download" defer=""></script><style>.blog-crv .item {
  display: flex;
  align-items: center;
  height: 100%;
}

.block-sec .testim-box .slick-dots li button {
  display: block;
  opacity: 0;
  width: 0;
  height: 0;
}

.slider .social-icon a {
  margin: 0 3px;
}

.navbar .navbar-nav .nav-link,
.video .vid .vid-butn .icon,
.video-wrapper .vid .vid-butn .icon {
  cursor: pointer;
}

.block-sec .vid-area {
  z-index: 99;
}

.div-tooltip-tit,
.div-tooltip-sub {
  display: block;
  padding: 0;
}

section.testimonials {
  overflow: hidden;
}

.contact-page .pages-header {
  overflow: hidden;
}

div#ieatmaps iframe {
  width: 100%;
  height: 100%;
  border: 0;
}

button.nb {
  background: transparent;
  color: #fff;
  cursor: pointer;
}

button.nb:hover {
  background: #fff;
  color: #222;
}

.replay {
  cursor: pointer;
}

.pace-done #preloader:after {
  bottom: 0;
}

#preloader {
  top: 0;
  left: 0;
}

.pace-done #preloader {
  visibility: hidden;
  transition-delay: 1.5s;
}

.pace-done #preloader:after,
.pace-done #preloader:before {
  height: 0;
  transition: all 0.7s cubic-bezier(1, 0, 0.55, 1);
  transition-delay: 1s;
}

body.hideX #preloader {
  display: none !important;
  z-index: -1111111;
  height: 0;
  width: 0;
  overflow: hidden;
}

body.hideX .pace {
  display: none !important;
  background-color: transparent;
}

.app-footer .social a {
  margin-right: 4px;
}
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9zcmMvc3R5bGVzL21haW4uc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNFLGFBQUE7RUFDQSxtQkFBQTtFQUNBLFlBQUE7QUFDRjs7QUFDQTtFQUNFLGNBQUE7RUFDQSxVQUFBO0VBQ0EsUUFBQTtFQUNBLFNBQUE7QUFFRjs7QUFBQTtFQUNFLGFBQUE7QUFHRjs7QUFEQTs7O0VBR0UsZUFBQTtBQUlGOztBQUZBO0VBQ0UsV0FBQTtBQUtGOztBQUhBOztFQUVFLGNBQUE7RUFDQSxVQUFBO0FBTUY7O0FBSkE7RUFDRSxnQkFBQTtBQU9GOztBQUxBO0VBQ0ksZ0JBQUE7QUFRSjs7QUFOQTtFQUNJLFdBQUE7RUFDQSxZQUFBO0VBQ0EsU0FBQTtBQVNKOztBQVBBO0VBQ0UsdUJBQUE7RUFDQSxXQUFBO0VBQ0EsZUFBQTtBQVVGOztBQVBBO0VBQ0UsZ0JBQUE7RUFDQSxXQUFBO0FBVUY7O0FBUkE7RUFDRSxlQUFBO0FBV0Y7O0FBUkE7RUFDRSxTQUFBO0FBV0Y7O0FBVEE7RUFDTSxNQUFBO0VBQ0YsT0FBQTtBQVlKOztBQVRBO0VBQ0Usa0JBQUE7RUFHQSxzQkFBQTtBQVlGOztBQVZBOztFQUVFLFNBQUE7RUFHQSxnREFBQTtFQUdBLG9CQUFBO0FBYUY7O0FBWEE7RUFDRSx3QkFBQTtFQUNBLGlCQUFBO0VBQ0EsU0FBQTtFQUNBLFFBQUE7RUFDQSxnQkFBQTtBQWNGOztBQVpBO0VBQ0Usd0JBQUE7RUFDQSw2QkFBQTtBQWVGOztBQWJBO0VBQ0UsaUJBQUE7QUFnQkYiLCJzb3VyY2VzQ29udGVudCI6WyIuYmxvZy1jcnYgLml0ZW0ge1xuICBkaXNwbGF5OiBmbGV4O1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICBoZWlnaHQ6IDEwMCU7XG59XG4uYmxvY2stc2VjIC50ZXN0aW0tYm94IC5zbGljay1kb3RzIGxpIGJ1dHRvbiB7XG4gIGRpc3BsYXk6IGJsb2NrO1xuICBvcGFjaXR5OiAwO1xuICB3aWR0aDogMDtcbiAgaGVpZ2h0OiAwO1xufVxuLnNsaWRlciAuc29jaWFsLWljb24gYSB7XG4gIG1hcmdpbjogMCAzcHg7XG59XG4ubmF2YmFyIC5uYXZiYXItbmF2IC5uYXYtbGluayxcbi52aWRlbyAudmlkIC52aWQtYnV0biAuaWNvbixcbi52aWRlby13cmFwcGVyIC52aWQgLnZpZC1idXRuIC5pY29uIHtcbiAgY3Vyc29yOiBwb2ludGVyO1xufVxuLmJsb2NrLXNlYyAudmlkLWFyZWEge1xuICB6LWluZGV4OiA5OTtcbn1cbi5kaXYtdG9vbHRpcC10aXQsXG4uZGl2LXRvb2x0aXAtc3ViIHtcbiAgZGlzcGxheTogYmxvY2s7XG4gIHBhZGRpbmc6IDA7XG59XG5zZWN0aW9uLnRlc3RpbW9uaWFscyB7XG4gIG92ZXJmbG93OiBoaWRkZW47XG59XG4uY29udGFjdC1wYWdlIC5wYWdlcy1oZWFkZXIge1xuICAgIG92ZXJmbG93OiBoaWRkZW47XG59XG5kaXYjaWVhdG1hcHMgaWZyYW1lIHtcbiAgICB3aWR0aDogMTAwJTtcbiAgICBoZWlnaHQ6IDEwMCU7XG4gICAgYm9yZGVyOiAwO1xufVxuYnV0dG9uLm5iIHtcbiAgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7XG4gIGNvbG9yOiAjZmZmO1xuICBjdXJzb3I6IHBvaW50ZXI7XG59XG5cbmJ1dHRvbi5uYjpob3ZlciB7XG4gIGJhY2tncm91bmQ6ICNmZmY7XG4gIGNvbG9yOiAjMjIyO1xufVxuLnJlcGxheSB7XG4gIGN1cnNvcjogcG9pbnRlcjtcbn1cblxuLnBhY2UtZG9uZSAjcHJlbG9hZGVyOmFmdGVyIHtcbiAgYm90dG9tOiAwO1xufVxuI3ByZWxvYWRlciB7XG4gICAgICB0b3A6IDA7XG4gICAgbGVmdDogMDs7XG59XG5cbi5wYWNlLWRvbmUgI3ByZWxvYWRlciB7XG4gIHZpc2liaWxpdHk6IGhpZGRlbjtcbiAgLXdlYmtpdC10cmFuc2l0aW9uLWRlbGF5OiAxLjVzO1xuICAtby10cmFuc2l0aW9uLWRlbGF5OiAxLjVzO1xuICB0cmFuc2l0aW9uLWRlbGF5OiAxLjVzO1xufVxuLnBhY2UtZG9uZSAjcHJlbG9hZGVyOmFmdGVyLFxuLnBhY2UtZG9uZSAjcHJlbG9hZGVyOmJlZm9yZSB7XG4gIGhlaWdodDogMDtcbiAgLXdlYmtpdC10cmFuc2l0aW9uOiBhbGwgMC43cyBjdWJpYy1iZXppZXIoMSwgMCwgMC41NSwgMSk7XG4gIC1vLXRyYW5zaXRpb246IGFsbCAwLjdzIGN1YmljLWJlemllcigxLCAwLCAwLjU1LCAxKTtcbiAgdHJhbnNpdGlvbjogYWxsIDAuN3MgY3ViaWMtYmV6aWVyKDEsIDAsIDAuNTUsIDEpO1xuICAtd2Via2l0LXRyYW5zaXRpb24tZGVsYXk6IDFzO1xuICAtby10cmFuc2l0aW9uLWRlbGF5OiAxcztcbiAgdHJhbnNpdGlvbi1kZWxheTogMXM7XG59XG5ib2R5LmhpZGVYICNwcmVsb2FkZXIge1xuICBkaXNwbGF5OiBub25lICFpbXBvcnRhbnQ7XG4gIHotaW5kZXg6IC0xMTExMTExO1xuICBoZWlnaHQ6IDA7XG4gIHdpZHRoOiAwO1xuICBvdmVyZmxvdzogaGlkZGVuO1xufVxuYm9keS5oaWRlWCAucGFjZSB7XG4gIGRpc3BsYXk6IG5vbmUgIWltcG9ydGFudDtcbiAgYmFja2dyb3VuZC1jb2xvcjogdHJhbnNwYXJlbnQ7XG59XG4uYXBwLWZvb3RlciAuc29jaWFsIGEge1xuICBtYXJnaW4tcmlnaHQ6IDRweDtcbn0iXSwic291cmNlUm9vdCI6IiJ9 */</style><style>:root {
  --toastify-color-light: #fff;
  --toastify-color-dark: #121212;
  --toastify-color-info: #3498db;
  --toastify-color-success: #07bc0c;
  --toastify-color-warning: #f1c40f;
  --toastify-color-error: #e74c3c;
  --toastify-color-transparent: rgba(255, 255, 255, 0.7);
  --toastify-icon-color-info: var(--toastify-color-info);
  --toastify-icon-color-success: var(--toastify-color-success);
  --toastify-icon-color-warning: var(--toastify-color-warning);
  --toastify-icon-color-error: var(--toastify-color-error);
  --toastify-toast-width: 320px;
  --toastify-toast-background: #fff;
  --toastify-toast-min-height: 64px;
  --toastify-toast-max-height: 800px;
  --toastify-font-family: sans-serif;
  --toastify-z-index: 9999;
  --toastify-text-color-light: #757575;
  --toastify-text-color-dark: #fff;
  --toastify-text-color-info: #fff;
  --toastify-text-color-success: #fff;
  --toastify-text-color-warning: #fff;
  --toastify-text-color-error: #fff;
  --toastify-spinner-color: #616161;
  --toastify-spinner-color-empty-area: #e0e0e0;
  --toastify-color-progress-light: linear-gradient(
    to right,
    #4cd964,
    #5ac8fa,
    #007aff,
    #34aadc,
    #5856d6,
    #ff2d55
  );
  --toastify-color-progress-dark: #bb86fc;
  --toastify-color-progress-info: var(--toastify-color-info);
  --toastify-color-progress-success: var(--toastify-color-success);
  --toastify-color-progress-warning: var(--toastify-color-warning);
  --toastify-color-progress-error: var(--toastify-color-error);
}

.Toastify__toast-container {
  z-index: var(--toastify-z-index);
  -webkit-transform: translate3d(0, 0, var(--toastify-z-index));
  position: fixed;
  padding: 4px;
  width: var(--toastify-toast-width);
  box-sizing: border-box;
  color: #fff;
}
.Toastify__toast-container--top-left {
  top: 1em;
  left: 1em;
}
.Toastify__toast-container--top-center {
  top: 1em;
  left: 50%;
  transform: translateX(-50%);
}
.Toastify__toast-container--top-right {
  top: 1em;
  right: 1em;
}
.Toastify__toast-container--bottom-left {
  bottom: 1em;
  left: 1em;
}
.Toastify__toast-container--bottom-center {
  bottom: 1em;
  left: 50%;
  transform: translateX(-50%);
}
.Toastify__toast-container--bottom-right {
  bottom: 1em;
  right: 1em;
}

@media only screen and (max-width : 480px) {
  .Toastify__toast-container {
    width: 100vw;
    padding: 0;
    left: 0;
    margin: 0;
  }
  .Toastify__toast-container--top-left, .Toastify__toast-container--top-center, .Toastify__toast-container--top-right {
    top: 0;
    transform: translateX(0);
  }
  .Toastify__toast-container--bottom-left, .Toastify__toast-container--bottom-center, .Toastify__toast-container--bottom-right {
    bottom: 0;
    transform: translateX(0);
  }
  .Toastify__toast-container--rtl {
    right: 0;
    left: auto;
    left: initial;
  }
}
.Toastify__toast {
  position: relative;
  min-height: var(--toastify-toast-min-height);
  box-sizing: border-box;
  margin-bottom: 1rem;
  padding: 8px;
  border-radius: 4px;
  box-shadow: 0 1px 10px 0 rgba(0, 0, 0, 0.1), 0 2px 15px 0 rgba(0, 0, 0, 0.05);
  display: flex;
  justify-content: space-between;
  max-height: var(--toastify-toast-max-height);
  overflow: hidden;
  font-family: var(--toastify-font-family);
  cursor: default;
  direction: ltr;
  /* webkit only issue #791 */
  z-index: 0;
}
.Toastify__toast--rtl {
  direction: rtl;
}
.Toastify__toast--close-on-click {
  cursor: pointer;
}
.Toastify__toast-body {
  margin: auto 0;
  flex: 1 1 auto;
  padding: 6px;
  display: flex;
  align-items: center;
}
.Toastify__toast-body > div:last-child {
  word-break: break-word;
  flex: 1 1;
}
.Toastify__toast-icon {
  margin-inline-end: 10px;
  width: 20px;
  flex-shrink: 0;
  display: flex;
}

.Toastify--animate {
  animation-fill-mode: both;
  animation-duration: 0.7s;
}

.Toastify--animate-icon {
  animation-fill-mode: both;
  animation-duration: 0.3s;
}

@media only screen and (max-width : 480px) {
  .Toastify__toast {
    margin-bottom: 0;
    border-radius: 0;
  }
}
.Toastify__toast-theme--dark {
  background: var(--toastify-color-dark);
  color: var(--toastify-text-color-dark);
}
.Toastify__toast-theme--light {
  background: var(--toastify-color-light);
  color: var(--toastify-text-color-light);
}
.Toastify__toast-theme--colored.Toastify__toast--default {
  background: var(--toastify-color-light);
  color: var(--toastify-text-color-light);
}
.Toastify__toast-theme--colored.Toastify__toast--info {
  color: var(--toastify-text-color-info);
  background: var(--toastify-color-info);
}
.Toastify__toast-theme--colored.Toastify__toast--success {
  color: var(--toastify-text-color-success);
  background: var(--toastify-color-success);
}
.Toastify__toast-theme--colored.Toastify__toast--warning {
  color: var(--toastify-text-color-warning);
  background: var(--toastify-color-warning);
}
.Toastify__toast-theme--colored.Toastify__toast--error {
  color: var(--toastify-text-color-error);
  background: var(--toastify-color-error);
}

.Toastify__progress-bar-theme--light {
  background: var(--toastify-color-progress-light);
}
.Toastify__progress-bar-theme--dark {
  background: var(--toastify-color-progress-dark);
}
.Toastify__progress-bar--info {
  background: var(--toastify-color-progress-info);
}
.Toastify__progress-bar--success {
  background: var(--toastify-color-progress-success);
}
.Toastify__progress-bar--warning {
  background: var(--toastify-color-progress-warning);
}
.Toastify__progress-bar--error {
  background: var(--toastify-color-progress-error);
}
.Toastify__progress-bar-theme--colored.Toastify__progress-bar--info, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--success, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--warning, .Toastify__progress-bar-theme--colored.Toastify__progress-bar--error {
  background: var(--toastify-color-transparent);
}

.Toastify__close-button {
  color: #fff;
  background: transparent;
  outline: none;
  border: none;
  padding: 0;
  cursor: pointer;
  opacity: 0.7;
  transition: 0.3s ease;
  align-self: flex-start;
}
.Toastify__close-button--light {
  color: #000;
  opacity: 0.3;
}
.Toastify__close-button > svg {
  fill: currentColor;
  height: 16px;
  width: 14px;
}
.Toastify__close-button:hover, .Toastify__close-button:focus {
  opacity: 1;
}

@keyframes Toastify__trackProgress {
  0% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
.Toastify__progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 5px;
  z-index: var(--toastify-z-index);
  opacity: 0.7;
  transform-origin: left;
}
.Toastify__progress-bar--animated {
  animation: Toastify__trackProgress linear 1 forwards;
}
.Toastify__progress-bar--controlled {
  transition: transform 0.2s;
}
.Toastify__progress-bar--rtl {
  right: 0;
  left: auto;
  left: initial;
  transform-origin: right;
}

.Toastify__spinner {
  width: 20px;
  height: 20px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: var(--toastify-spinner-color-empty-area);
  border-right-color: var(--toastify-spinner-color);
  animation: Toastify__spin 0.65s linear infinite;
}

@keyframes Toastify__bounceInRight {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  from {
    opacity: 0;
    transform: translate3d(3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(-25px, 0, 0);
  }
  75% {
    transform: translate3d(10px, 0, 0);
  }
  90% {
    transform: translate3d(-5px, 0, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
}
@keyframes Toastify__bounceInLeft {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(25px, 0, 0);
  }
  75% {
    transform: translate3d(-10px, 0, 0);
  }
  90% {
    transform: translate3d(5px, 0, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutLeft {
  20% {
    opacity: 1;
    transform: translate3d(20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(-2000px, 0, 0);
  }
}
@keyframes Toastify__bounceInUp {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  from {
    opacity: 0;
    transform: translate3d(0, 3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  75% {
    transform: translate3d(0, 10px, 0);
  }
  90% {
    transform: translate3d(0, -5px, 0);
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__bounceOutUp {
  20% {
    transform: translate3d(0, -10px, 0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0, 20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, -2000px, 0);
  }
}
@keyframes Toastify__bounceInDown {
  from, 60%, 75%, 90%, to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0, -3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, 25px, 0);
  }
  75% {
    transform: translate3d(0, -10px, 0);
  }
  90% {
    transform: translate3d(0, 5px, 0);
  }
  to {
    transform: none;
  }
}
@keyframes Toastify__bounceOutDown {
  20% {
    transform: translate3d(0, 10px, 0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, 2000px, 0);
  }
}
.Toastify__bounce-enter--top-left, .Toastify__bounce-enter--bottom-left {
  animation-name: Toastify__bounceInLeft;
}
.Toastify__bounce-enter--top-right, .Toastify__bounce-enter--bottom-right {
  animation-name: Toastify__bounceInRight;
}
.Toastify__bounce-enter--top-center {
  animation-name: Toastify__bounceInDown;
}
.Toastify__bounce-enter--bottom-center {
  animation-name: Toastify__bounceInUp;
}

.Toastify__bounce-exit--top-left, .Toastify__bounce-exit--bottom-left {
  animation-name: Toastify__bounceOutLeft;
}
.Toastify__bounce-exit--top-right, .Toastify__bounce-exit--bottom-right {
  animation-name: Toastify__bounceOutRight;
}
.Toastify__bounce-exit--top-center {
  animation-name: Toastify__bounceOutUp;
}
.Toastify__bounce-exit--bottom-center {
  animation-name: Toastify__bounceOutDown;
}

@keyframes Toastify__zoomIn {
  from {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
@keyframes Toastify__zoomOut {
  from {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  to {
    opacity: 0;
  }
}
.Toastify__zoom-enter {
  animation-name: Toastify__zoomIn;
}

.Toastify__zoom-exit {
  animation-name: Toastify__zoomOut;
}

@keyframes Toastify__flipIn {
  from {
    transform: perspective(400px) rotate3d(1, 0, 0, 90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotate3d(1, 0, 0, 10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotate3d(1, 0, 0, -5deg);
  }
  to {
    transform: perspective(400px);
  }
}
@keyframes Toastify__flipOut {
  from {
    transform: perspective(400px);
  }
  30% {
    transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
    opacity: 1;
  }
  to {
    transform: perspective(400px) rotate3d(1, 0, 0, 90deg);
    opacity: 0;
  }
}
.Toastify__flip-enter {
  animation-name: Toastify__flipIn;
}

.Toastify__flip-exit {
  animation-name: Toastify__flipOut;
}

@keyframes Toastify__slideInRight {
  from {
    transform: translate3d(110%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInLeft {
  from {
    transform: translate3d(-110%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInUp {
  from {
    transform: translate3d(0, 110%, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideInDown {
  from {
    transform: translate3d(0, -110%, 0);
    visibility: visible;
  }
  to {
    transform: translate3d(0, 0, 0);
  }
}
@keyframes Toastify__slideOutRight {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(110%, 0, 0);
  }
}
@keyframes Toastify__slideOutLeft {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(-110%, 0, 0);
  }
}
@keyframes Toastify__slideOutDown {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, 500px, 0);
  }
}
@keyframes Toastify__slideOutUp {
  from {
    transform: translate3d(0, 0, 0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, -500px, 0);
  }
}
.Toastify__slide-enter--top-left, .Toastify__slide-enter--bottom-left {
  animation-name: Toastify__slideInLeft;
}
.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right {
  animation-name: Toastify__slideInRight;
}
.Toastify__slide-enter--top-center {
  animation-name: Toastify__slideInDown;
}
.Toastify__slide-enter--bottom-center {
  animation-name: Toastify__slideInUp;
}

.Toastify__slide-exit--top-left, .Toastify__slide-exit--bottom-left {
  animation-name: Toastify__slideOutLeft;
}
.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right {
  animation-name: Toastify__slideOutRight;
}
.Toastify__slide-exit--top-center {
  animation-name: Toastify__slideOutUp;
}
.Toastify__slide-exit--bottom-center {
  animation-name: Toastify__slideOutDown;
}

@keyframes Toastify__spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/*# sourceMappingURL=ReactToastify.css.map */
/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9ub2RlX21vZHVsZXMvcmVhY3QtdG9hc3RpZnkvc2Nzcy9fdmFyaWFibGVzLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L2Rpc3QvUmVhY3RUb2FzdGlmeS5jc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX3RvYXN0Q29udGFpbmVyLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX3RvYXN0LnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX3RoZW1lLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX2Nsb3NlQnV0dG9uLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX3Byb2dyZXNzQmFyLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvX2ljb25zLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvYW5pbWF0aW9ucy9fYm91bmNlLnNjc3MiLCJ3ZWJwYWNrOi8vbm9kZV9tb2R1bGVzL3JlYWN0LXRvYXN0aWZ5L3Njc3MvYW5pbWF0aW9ucy9fem9vbS5zY3NzIiwid2VicGFjazovL25vZGVfbW9kdWxlcy9yZWFjdC10b2FzdGlmeS9zY3NzL2FuaW1hdGlvbnMvX2ZsaXAuc2NzcyIsIndlYnBhY2s6Ly9ub2RlX21vZHVsZXMvcmVhY3QtdG9hc3RpZnkvc2Nzcy9hbmltYXRpb25zL19zbGlkZS5zY3NzIiwid2VicGFjazovL25vZGVfbW9kdWxlcy9yZWFjdC10b2FzdGlmeS9zY3NzL2FuaW1hdGlvbnMvX3NwaW4uc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFHQTtFQUNFLDRCQUFBO0VBQ0EsOEJBQUE7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 */</style><noscript id="__next_css__DO_NOT_USE__"></noscript><style data-styled="active" data-styled-version="6.0.7">.fDbOgA{position:relative;box-sizing:border-box;display:flex;flex-direction:column;width:100%;height:100%;max-width:100%;color:#ffffff;background-color:transparent;}.VQFza{display:flex;width:100%;color:#ffffff;font-size:12px;font-weight:500;}.fMNPoN{display:flex;align-items:stretch;width:100%;background-color:transparent;min-height:52px;border-bottom-width:1px;border-bottom-color:rgba(255, 255, 255, 0.05);border-bottom-style:solid;}.dHwQJD{position:relative;display:flex;align-items:center;box-sizing:border-box;line-height:normal;padding-left:16px;padding-right:16px;}.hRfGpm{position:relative;display:flex;align-items:center;box-sizing:border-box;line-height:normal;padding-left:16px;padding-right:16px;word-break:break-word;}.bgjZIa{flex-grow:1;flex-shrink:0;flex-basis:0;max-width:100%;min-width:100px;min-width:5%;max-width:5%;}.eMcYIW{flex-grow:1;flex-shrink:0;flex-basis:0;max-width:100%;min-width:100px;min-width:50%;max-width:50%;}.dmbIjK{flex-grow:1;flex-shrink:0;flex-basis:0;max-width:100%;min-width:100px;min-width:15%;max-width:15%;}.dahnUA div:first-child{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}.eDlsWh{display:flex;align-items:stretch;align-content:stretch;width:100%;box-sizing:border-box;font-size:13px;font-weight:400;color:#ffffff;background-color:transparent;min-height:48px;}.eDlsWh:not(:last-of-type){border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:rgba(255, 255, 255, 0.05);}.eDlsWh:hover{color:#FFFFFF;background-color:rgba(0, 0, 0, .7);transition-duration:0.15s;transition-property:background-color;border-bottom-color:transparent;outline-style:solid;outline-width:1px;outline-color:transparent;}.cAqGqO{padding:2px;color:inherit;flex-grow:0;flex-shrink:0;opacity:0;}.beICJd{display:inline-flex;align-items:center;justify-content:inherit;height:100%;width:100%;outline:none;user-select:none;overflow:hidden;cursor:pointer;}.beICJd span.__rdt_custom_sort_icon__ i,.beICJd span.__rdt_custom_sort_icon__ svg{transform:'translate3d(0, 0, 0)';opacity:0;color:inherit;font-size:18px;height:18px;width:18px;backface-visibility:hidden;transform-style:preserve-3d;transition-duration:95ms;transition-property:transform;}.beICJd span.__rdt_custom_sort_icon__.asc i,.beICJd span.__rdt_custom_sort_icon__.asc svg{transform:rotate(180deg);}.beICJd:hover,.beICJd:focus{opacity:0.7;}.beICJd:hover span,.beICJd:focus span,.beICJd:hover span.__rdt_custom_sort_icon__ *,.beICJd:focus span.__rdt_custom_sort_icon__ *{opacity:0.7;}.ggomLY{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}.fWlzdU{display:flex;flex-direction:column;}.LYwHa{position:relative;width:100%;border-radius:inherit;overflow-x:auto;overflow-y:hidden;min-height:0;}.eRHmuV{position:relative;width:100%;display:table;}.jznLPr{box-sizing:border-box;width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:#ffffff;background-color:transparent;}.ippUbX{cursor:pointer;height:24px;max-width:100%;user-select:none;padding-left:8px;padding-right:24px;box-sizing:content-box;font-size:inherit;color:inherit;border:none;background-color:transparent;appearance:none;direction:ltr;flex-shrink:0;}.ippUbX::-ms-expand{display:none;}.ippUbX:disabled::-ms-expand{background:#f60;}.ippUbX option{color:initial;}.jfFaHg{position:relative;flex-shrink:0;font-size:inherit;color:inherit;margin-top:1px;}.jfFaHg svg{top:0;right:0;color:inherit;position:absolute;fill:currentColor;width:24px;height:24px;display:inline-block;user-select:none;pointer-events:none;}.HurfU{display:flex;flex:1 1 auto;justify-content:flex-end;align-items:center;box-sizing:border-box;padding-right:8px;padding-left:8px;width:100%;color:#2aa198;font-size:13px;min-height:56px;background-color:transparent;border-top-style:solid;border-top-width:1px;border-top-color:rgba(255, 255, 255, 0.05);}.fMuUAw{position:relative;display:block;user-select:none;border:none;border-radius:50%;height:40px;width:40px;padding:8px;margin:px;cursor:pointer;transition:0.4s;color:#FFFFFF;fill:#FFFFFF;background-color:transparent;}.fMuUAw:disabled{cursor:unset;color:rgba(255, 255, 255, .18);fill:rgba(255, 255, 255, .18);}.fMuUAw:hover:not(:disabled){background-color:rgba(255, 255, 255, .12);}.fMuUAw:focus{outline:none;background-color:rgba(255, 255, 255, .54);}.fKJrIg{display:flex;align-items:center;border-radius:4px;white-space:nowrap;}@media screen and (max-width: 599px){.fKJrIg{width:100%;justify-content:space-around;}}.efFWSV{flex-shrink:1;user-select:none;}.jeKBgP{margin:0 24px;}.kMfkEy{margin:0 4px;}</style><script async="async" type="text/javascript" src="./Sum of an Array in Given Range_files/editor.main.js.download"></script><script async="async" type="text/javascript" src="./Sum of an Array in Given Range_files/editor.main.nls.js.download"></script><script async="async" type="text/javascript" src="./Sum of an Array in Given Range_files/python.js.download"></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #ffffff;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.8);
--vscode-editorInlayHint-typeForeground: #ffffff;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.8);
--vscode-editorInlayHint-parameterForeground: #ffffff;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.8);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.2);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.2);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.2);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.2);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #252526;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: rgba(55, 148, 255, 0.1);
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #569cd6; }
.mtk9 { color: #dcdcdc; }
.mtk10 { color: #808080; }
.mtk11 { color: #f44747; }
.mtk12 { color: #c586c0; }
.mtk13 { color: #a79873; }
.mtk14 { color: #dd6a6f; }
.mtk15 { color: #5bb498; }
.mtk16 { color: #909090; }
.mtk17 { color: #778899; }
.mtk18 { color: #ff00ff; }
.mtk19 { color: #b46695; }
.mtk20 { color: #ff0000; }
.mtk21 { color: #4f76ac; }
.mtk22 { color: #3dc9b0; }
.mtk23 { color: #74b0df; }
.mtk24 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="pace-done pace-done pace-done "><div class="pace pace-inactive"><div class="pace-progress" data-progress-text="100%" data-progress="99" style="transform: translate3d(100%, 0px, 0px);">
  <div class="pace-progress-inner"></div>
</div>
<div class="pace-activity"></div></div><div id="__next" data-reactroot=""><div class="mouse-cursor cursor-outer cursor-hover" style="visibility: visible; transform: translate(947px, 443px);"></div><div class="mouse-cursor cursor-inner cursor-hover" style="visibility: visible; transform: translate(947px, 443px);"></div><div class="showX"><div class="loading isdone"><span>O</span><span>W</span><span>L</span><span>C</span><span>O</span><span>D</span><span>E</span><span>R</span></div><div id="preloader" class="isdone"></div></div><div class="circle-bg"><div class="circle-color fixed"><div class="gradient-circle"></div><div class="gradient-circle two"></div></div></div><nav class="navbar navbar-expand-lg change"><div class="container"><a class="logo" href="https://owlcoder.technicalhub.io/"><img src="./Sum of an Array in Given Range_files/logo-light.png" class="logo img_size" alt="logo"></a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="icon-bar"><i class="fas fa-bars"></i></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav ml-auto"><li class="nav-item"></li><li class="nav-item"><a class="nav-link" href="https://owlcoder.technicalhub.io/homepage/home5-dark/">Home</a></li><li class="nav-item"><a class="nav-link" href="https://owlcoder.technicalhub.io/about/about-dark/">About</a></li><li class="nav-item"><a class="nav-link" href="https://owlcoder.technicalhub.io/level-course-grid/level-course-grid-dark/">Courses</a></li><li class="nav-item" id="_link"><a class="nav-link" href="https://owlcoder.technicalhub.io/contact/contact-dark/">Contact</a></li><li class="nav-item" id="_link"></li><li class="nav-item dropdown"><div class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Profile</div><div class="dropdown-menu" style="display: flex; flex-direction: column; align-items: center;"><img src="./Sum of an Array in Given Range_files/defaultUser.png" style="width: 35px; border-radius: 50%;"><span class="dropdown-item">NARUKULAJOHNWESLY -</span><span class="dropdown-item" style="cursor: pointer;">Logout</span></div></li><li class="nav-item"></li></ul></div></div></nav><section class="blog-pg blog-list compiler-section-padding pt-0"><div class="Toastify"></div><div class="container-fluid sub-bg"><div class="row justify-content-center"><div class="col-lg-11"><div class="posts mt-80"><div class="item mb-80 wow fadeInUp" data-wow-delay=".3s" style="visibility: visible; animation-delay: 0.3s;"><div class="row"><div class="col-lg-6 "><div class="cont"><div class="program_data"><div class="info"><a class="tag"><span>Level-1</span></a><span>/</span><a class="tag"><span>easy</span></a><span>/</span><a class="tag"><span>Points: 20</span></a></div><h5 class="program_heading"><a>Sum of an Array in Given Range</a></h5><h6 class="sub-heading">Program Description :</h6><p class="mt-10 program_desc"><p>given an array of N integers, a lower bound, a upper bound. print the sum of all elements between these range.</p>
</p><h6 class="sub-heading">Input Format :</h6><p class="mt-10 input_format"><p>first line comtains an integer N, where N is length of an array</p>
<p>second line contains N spaced integers</p>
<p>third line contains lower bond from where the sum of the elements starts</p>
<p>fourth line contains upper bond the end index of the sum</p>
<p>Note:</p>
<p>index starts from 0&nbsp;</p>
</p><h6 class="sub-heading">Output Format :</h6><p class="mt-10 output_format"><p>integer value</p>
</p><h6 class="sub-heading">Input :</h6><p class="mt-10 input"><code><p>6</p>
<p>1 2 3 4 5 6</p>
<p>3</p>
<p>5&nbsp;</p>
</code></p><h6 class="sub-heading">Output :</h6><p class="mt-10 output"><code><p>15</p>
</code></p><h6 class="sub-heading">Constraints :</h6><p class="mt-10 constraints"><p>0&lt;=n&lt;=10^6</p>
<p>0&lt;=a[i]&lt;=10^6</p>
<p>0&lt;=n1&lt;=10^6</p>
<p>0&lt;=n2&lt;=10^6</p>
</p></div></div></div><div class="col-lg-6 compiler"><div class="options"><div class="optionsPart1"><div class="col-lg-6 form-group"><select id="lang" name="lang" required="" fdprocessedid="ztgyvdf"><option value="c">C  -  GCC 11.1.0</option><option value="cpp">C++  -  GCC 11.1.0</option><option value="python">Python3  -  3.9.9</option><option value="java">Java  -  JDK 17.0.1</option></select></div><div class="timer"><button class="d-none" fdprocessedid="z7wcul"><i class="pe-7s-timer"></i>Start Timer</button><span id="counter" class="d-block" style="padding: 10px;">Timer : 9:42</span></div></div><div title="Reset" class="optionsPart2"><span style="padding: 20px;"><i class="pe-7s-expand1"></i></span><span style="padding: 20px;"><i class="pe-7s-refresh"></i></span></div></div><section style="display: flex; position: relative; text-align: initial; height: 70vh;"><div class="EditorHeight" style="width: 100%; --vscode-editorCodeLens-lineHeight: 21px; --vscode-editorCodeLens-fontSize: 15px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;" data-keybinding-context="1" data-mode-id="python"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark focused" role="code" data-uri="inmemory://model/1" style="width: 666px; height: 495px;"><div data-mprt="3" class="overflow-guard" style="width: 666px; height: 495px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 783px; width: 73px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 783px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 17px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 24px; letter-spacing: 0px; width: 73px; height: 783px;"><div style="position:absolute;top:144px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">7</div></div><div style="position:absolute;top:168px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">8</div></div><div style="position:absolute;top:192px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">9</div></div><div style="position:absolute;top:240px;width:100%;height:24px;"><div class="current-line current-line-margin-both" style="width:73px; height:24px;"></div><div class="line-numbers active-line-number" style="left:0px;width:47px;">11</div></div><div style="position:absolute;top:120px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">6</div></div><div style="position:absolute;top:96px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">5</div></div><div style="position:absolute;top:72px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">4</div></div><div style="position:absolute;top:48px;width:100%;height:24px;"><div class="cldr codicon codicon-folding-expanded" style="left:47px;width:26px;"></div><div class="line-numbers" style="left:0px;width:47px;">3</div></div><div style="position:absolute;top:24px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">2</div></div><div style="position:absolute;top:0px;width:100%;height:24px;"><div class="cldr codicon codicon-folding-expanded" style="left:47px;width:26px;"></div><div class="line-numbers" style="left:0px;width:47px;">1</div></div><div style="position:absolute;top:216px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">10</div></div><div style="position:absolute;top:264px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">12</div></div><div style="position:absolute;top:288px;width:100%;height:24px;"><div class="line-numbers" style="left:0px;width:47px;">13</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 73px; height: 495px; width: 593px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays focused" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 17px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 24px; letter-spacing: 0px; height: 0px; width: 2192px;"><div style="position:absolute;top:144px;width:100%;height:24px;"></div><div style="position:absolute;top:168px;width:100%;height:24px;"></div><div style="position:absolute;top:192px;width:100%;height:24px;"></div><div style="position:absolute;top:240px;width:100%;height:24px;"><div class="current-line" style="width:2192px; height:24px;"></div><div class="cdr wordHighlightText" style="left:84px;width:75px;height:24px;"></div></div><div style="position:absolute;top:120px;width:100%;height:24px;"></div><div style="position:absolute;top:96px;width:100%;height:24px;"><div class="core-guide core-guide-indent vertical" style="left:0px;height:24px;width:9.34765625px"></div></div><div style="position:absolute;top:72px;width:100%;height:24px;"><div class="core-guide core-guide-indent vertical" style="left:0px;height:24px;width:9.34765625px"></div><div class="core-guide core-guide-indent vertical" style="left:37.390625px;height:24px;width:9.34765625px"></div></div><div style="position:absolute;top:48px;width:100%;height:24px;"><div class="core-guide core-guide-indent vertical" style="left:0px;height:24px;width:9.34765625px"></div></div><div style="position:absolute;top:24px;width:100%;height:24px;"><div class="core-guide core-guide-indent vertical" style="left:0px;height:24px;width:9.34765625px"></div></div><div style="position:absolute;top:0px;width:100%;height:24px;"><div class="cdr wordHighlightText" style="left:37px;width:75px;height:24px;"></div></div><div style="position:absolute;top:216px;width:100%;height:24px;"></div><div style="position:absolute;top:264px;width:100%;height:24px;"></div><div style="position:absolute;top:288px;width:100%;height:24px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 17px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 24px; letter-spacing: 0px; width: 2192px; height: 783px;"><div style="top:144px;height:24px;" class="view-line"><span><span class="mtk1">L&nbsp;=&nbsp;</span><span class="mtk8">list</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk8">map</span><span class="mtk9 bracket-highlighting-1">(</span><span class="mtk8">int</span><span class="mtk9">,</span><span class="mtk8">input</span><span class="mtk9 bracket-highlighting-2">(</span><span class="mtk9 bracket-highlighting-2">)</span><span class="mtk1">.split</span><span class="mtk9 bracket-highlighting-2">(</span><span class="mtk9 bracket-highlighting-2">)</span><span class="mtk9 bracket-highlighting-1">)</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:168px;height:24px;" class="view-line"><span><span class="mtk1">a&nbsp;=&nbsp;</span><span class="mtk8">int</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk8">input</span><span class="mtk9 bracket-highlighting-1">(</span><span class="mtk9 bracket-highlighting-1">)</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:192px;height:24px;" class="view-line"><span><span class="mtk1">b&nbsp;=&nbsp;</span><span class="mtk8">int</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk8">input</span><span class="mtk9 bracket-highlighting-1">(</span><span class="mtk9 bracket-highlighting-1">)</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top: 240px; height: 24px;" class="view-line"><span><span class="mtk1">result&nbsp;=&nbsp;sumRange</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk1">L</span><span class="mtk9">,</span><span class="mtk1">a</span><span class="mtk9">,</span><span class="mtk1">b</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:120px;height:24px;" class="view-line"><span><span class="mtk1">n=</span><span class="mtk8">int</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk8">input</span><span class="mtk9 bracket-highlighting-1">(</span><span class="mtk9 bracket-highlighting-1">)</span><span class="mtk9 bracket-highlighting-0">)</span></span></div><div style="top:96px;height:24px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">return</span><span class="mtk1">&nbsp;</span><span class="mtk8">sum</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:72px;height:24px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">sum</span><span class="mtk1">&nbsp;+=&nbsp;L</span><span class="mtk9 bracket-highlighting-0">[</span><span class="mtk1">i</span><span class="mtk9 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:48px;height:24px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">for</span><span class="mtk1">&nbsp;i&nbsp;</span><span class="mtk8">in</span><span class="mtk1">&nbsp;</span><span class="mtk8">range</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk1">a</span><span class="mtk9">,</span><span class="mtk1">b+</span><span class="mtk6">1</span><span class="mtk9">,</span><span class="mtk6">1</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk9">:</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:24px;height:24px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">sum</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk6">0</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;</span></span></div><div style="top:0px;height:24px;" class="view-line"><span><span class="mtk8">def</span><span class="mtk1">&nbsp;sumRange</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk1">L</span><span class="mtk9">,</span><span class="mtk1">a</span><span class="mtk9">,</span><span class="mtk1">b</span><span class="mtk9 bracket-highlighting-0">)</span><span class="mtk9">:</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:216px;height:24px;" class="view-line"><span><span></span></span></div><div style="top:264px;height:24px;" class="view-line"><span><span></span></span></div><div style="top:288px;height:24px;" class="view-line"><span><span class="mtk8">print</span><span class="mtk9 bracket-highlighting-0">(</span><span class="mtk1">result</span><span class="mtk9 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 24px; top: 240px; left: 103px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 17px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 24px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="visible scrollbar horizontal" style="position: absolute; width: 526px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 4px; left: 0px; height: 4px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 129px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="618" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 495px; display: block;"></canvas><div role="presentation" aria-hidden="true" class="visible scrollbar vertical" style="position: absolute; width: 14px; height: 495px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: -2px; width: 18px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 312px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 652px;" class=""></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 37.3906px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 17px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 24px; letter-spacing: 0px; top: 240px; left: 176px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover line-numbers"></div><div data-mprt="4" class="overlayWidgets" style="width: 666px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 599px; width: 53px; height: 495px;"><div class="minimap-shadow-visible" style="height: 495px;"></div><canvas width="66" height="618" style="position: absolute; left: 0px; width: 52.8px; height: 494.4px;"></canvas><canvas class="minimap-decorations-layer" width="66" height="618" style="position: absolute; left: 0px; width: 52.8px; height: 494.4px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 53px; display: block; top: 0px; height: 33px;"><div class="minimap-slider-horizontal" style="position: absolute; left: 0px; width: 53px; top: 0px; height: 33px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.contentHoverWidget" style="position: absolute; display: none; visibility: hidden; max-width: 1536px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 17px; line-height: 1.41176; max-height: 250px; max-width: 500px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div><div class="editor-widget suggest-widget" widgetid="editor.widget.suggestWidget" style="position: absolute; display: none; visibility: hidden; max-width: 1536px; height: 26px; width: 430px; top: 144px; left: 176px;"><div class="monaco-sash vertical" style="left: 428px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal disabled" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 24px;"><div class="orthogonal-drag-handle end"></div></div><div class="message" aria-hidden="true" style="display: none;"></div><div class="tree" style="height: 26px; display: none;" aria-hidden="true"><div class="monaco-list list_id_1 selection-none" tabindex="0" role="listbox" aria-label="Suggest"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-list-rows" style="transform: translate3d(0px, 0px, 0px); overflow: hidden; contain: strict; height: 0px; left: 0px; top: 0px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 0px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 26px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 26px;"></div></div></div><style type="text/css" media="screen">.monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: var(--vscode-list-focusBackground); }
.monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: var(--vscode-list-focusBackground); }
.monaco-list.list_id_1:focus .monaco-list-row.focused { color: var(--vscode-list-focusForeground); }
.monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: var(--vscode-list-activeSelectionBackground); }
.monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: var(--vscode-list-activeSelectionBackground); }
.monaco-list.list_id_1:focus .monaco-list-row.selected { color: var(--vscode-list-activeSelectionForeground); }
.monaco-list.list_id_1:focus .monaco-list-row.selected .codicon { color: var(--vscode-list-activeSelectionIconForeground); }

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: var(--vscode-list-activeSelectionBackground); }
			

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: var(--vscode-list-activeSelectionForeground); }
			
.monaco-list.list_id_1 .monaco-list-row.focused .codicon { color:  var(--vscode-list-inactiveSelectionIconForeground); }
.monaco-list.list_id_1 .monaco-list-row.focused { background-color:  var(--vscode-editorSuggestWidget-selectedBackground); }
.monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color:  var(--vscode-editorSuggestWidget-selectedBackground); }
.monaco-list.list_id_1 .monaco-list-row.selected { background-color:  var(--vscode-list-inactiveSelectionBackground); }
.monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color:  var(--vscode-list-inactiveSelectionBackground); }
.monaco-list.list_id_1 .monaco-list-row.selected { color: var(--vscode-list-inactiveSelectionForeground); }
.monaco-list.list_id_1:not(.drop-target):not(.dragging) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: var(--vscode-list-hoverBackground); }
.monaco-list.list_id_1:not(.drop-target):not(.dragging) .monaco-list-row:hover:not(.selected):not(.focused) { color:  var(--vscode-list-hoverForeground); }
.monaco-list.list_id_1:focus .monaco-list-row.focused.selected { outline: 1px solid var(--vscode-list-focusAndSelectionOutline, var(--vscode-contrastActiveBorder, var(--vscode-list-focusOutline))); outline-offset: -1px;}

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.focused { outline: 1px solid var(--vscode-list-focusOutline); outline-offset: -1px; }
				.monaco-workbench.context-menu-visible .monaco-list.list_id_1.last-focused .monaco-list-row.focused { outline: 1px solid var(--vscode-list-focusOutline); outline-offset: -1px; }
			
.monaco-list.list_id_1 .monaco-list-row.focused.selected { outline: 1px dotted var(--vscode-contrastActiveBorder, var(--vscode-contrastActiveBorder)); outline-offset: -1px; }
.monaco-list.list_id_1 .monaco-list-row.selected { outline: 1px dotted var(--vscode-contrastActiveBorder); outline-offset: -1px; }
.monaco-list.list_id_1 .monaco-list-row.focused { outline: 1px dotted var(--vscode-contrastActiveBorder); outline-offset: -1px; }
.monaco-list.list_id_1 .monaco-list-row:hover { outline: 1px dashed var(--vscode-contrastActiveBorder); outline-offset: -1px; }

				.monaco-list.list_id_1.drop-target,
				.monaco-list.list_id_1 .monaco-list-rows.drop-target,
				.monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: var(--vscode-list-dropBackground) !important; color: inherit !important; }
			

				.monaco-table > .monaco-split-view2,
				.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before,
				.monaco-workbench:not(.reduce-motion) .monaco-table:hover > .monaco-split-view2,
				.monaco-workbench:not(.reduce-motion) .monaco-table:hover > .monaco-split-view2 .monaco-sash.vertical::before {
					border-color: var(--vscode-tree-tableColumnsBorder);
				}

				.monaco-workbench:not(.reduce-motion) .monaco-table > .monaco-split-view2,
				.monaco-workbench:not(.reduce-motion) .monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
					border-color: transparent;
				}
			

				.monaco-table .monaco-list-row[data-parity=odd]:not(.focused):not(.selected):not(:hover) .monaco-table-tr,
				.monaco-table .monaco-list:not(:focus) .monaco-list-row[data-parity=odd].focused:not(.selected):not(:hover) .monaco-table-tr,
				.monaco-table .monaco-list:not(.focused) .monaco-list-row[data-parity=odd].focused:not(.selected):not(:hover) .monaco-table-tr {
					background-color: var(--vscode-tree-tableOddRowsBackground);
				}
			</style></div></div><div class="suggest-status-bar" style="height: 24px; display: none;" aria-hidden="true"><div class="monaco-action-bar animated left"><ul class="actions-container" role="presentation"><li class="action-item menu-entry" role="presentation" title="Insert (Enter)"><a class="action-label" role="button" aria-label="Insert (Enter)" tabindex="0">Insert (⏎)</a></li></ul></div><div class="monaco-action-bar animated right"><ul class="actions-container" role="presentation"><li class="action-item menu-entry" role="presentation" title="show more (Ctrl+Space)"><a class="action-label" role="button" aria-label="show more (Ctrl+Space)" tabindex="0">show more (Ctrl+Space)</a></li></ul></div></div></div></div></div></div></section><div class="btn-more mt-30 row"><div class="col-md-6"><button class="simple-btn btn btn-primary text-left" fdprocessedid="ug7ds">Run Code</button></div><div class="d-none"><button class="simple-btn btn btn-success" fdprocessedid="77615p">Submit Code</button></div></div><br><div class="text-center"><div></div></div><div class="table-responsive"><table class="d-none"><thead class="table-dark"><tr><th>#</th><th>expected output</th><th>output</th><th>memory</th><th>cpuTime</th><th>result</th></tr></thead><tbody><tr><td>case-1</td><td>15</td><td>15</td><td>7852</td><td>0.00</td><td class="text-success">pass</td></tr><tr><td>case-2</td><td>18</td><td>18</td><td>7848</td><td>0.01</td><td class="text-success">pass</td></tr></tbody></table></div><div class="d-none"><p>All Hidden test cases passed</p></div><div class="table-responsive"><table class="d-none"><tbody><tr><td>Hidden case-1</td><td class="text-success">pass</td></tr><tr><td>Hidden case-2</td><td class="text-success">pass</td></tr></tbody></table></div></div></div></div></div></div></div></div></section></div><div id="modal-portal"></div><script src="./Sum of an Array in Given Range_files/react-refresh.js.download"></script><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{}},"page":"/login/login-dark","query":{},"buildId":"development","nextExport":true,"autoExport":true,"isFallback":false,"scriptLoader":[]}</script><script src="./Sum of an Array in Given Range_files/wow.min.js.download" id="wow" data-nscript="afterInteractive"></script><next-route-announcer><p aria-live="assertive" id="__next-route-announcer__" role="alert" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; white-space: nowrap; overflow-wrap: normal;">OwlCoder</p></next-route-announcer><script id="wowInit" data-nscript="lazyOnload"></script><script src="./Sum of an Array in Given Range_files/level-course-grid-dark.js.download"></script><script src="./Sum of an Array in Given Range_files/[name].js.download"></script><script src="./Sum of an Array in Given Range_files/[id].js.download"></script><script src="./Sum of an Array in Given Range_files/loader.js.download"></script><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div></body></html>