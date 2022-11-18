<template>
  <div id="app">
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import config from '../../package.json';

export default {
  name: 'client-demo',
  components: {
  },
  data() {
    return {
      isLogin: false,
    };
  },
  async created() {
    document.title = `client-demo V${config.version}`;
  },
  methods: {

  },
};
</script>

<style lang="less">
* {
  margin: 0;
  padding: 0;
}
#app {
  height: 100%;
}
</style>
