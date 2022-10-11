<template>
<div @click="start">{{ tips }}</div>
</template>

<script>
import { ipcRenderer } from 'electron';

export default {
  name: 'home',
  data() {
    return {
      tips: '开始',
    };
  },
  methods: {
    start() {
      console.log(1234);
      ipcRenderer.send('start');

      ipcRenderer.on('start', (event, data) => {
        console.log(event, data);
        this.tips = data;
      });
    },
  },
};
</script>

<style scoped>

</style>
