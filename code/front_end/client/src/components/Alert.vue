<template>
  <div>
    <b-alert v-bind:variant="alter_variant" show>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'alter_variant'],
};
</script>
