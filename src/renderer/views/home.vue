<template>
<div @click="start">阿斯达四大</div>
</template>

<script>
import { ipcRenderer } from 'electron';

export default {
  name: 'home',
  methods: {
    start() {
      console.log(1234);
      ipcRenderer.send('start');

      ipcRenderer.on('start', (event, data) => {
        console.log(event, data);
      });
    },
  },
};
</script>

<style scoped>

</style>
