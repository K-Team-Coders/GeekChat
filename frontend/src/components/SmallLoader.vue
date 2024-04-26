<template>
  <div>
    <span class="loader"></span>
  </div>
</template>

<script>
export default {};
</script>

<style>
.loader {
  width: 40px;
  height: 40px;
  border: 3px solid #7c7c7c;
  border-bottom-color: transparent;
  border-radius: 50%;
  display: inline-block;
  box-sizing: border-box;
  animation: rotation 1s linear infinite;
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
