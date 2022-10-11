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
#app {
  height: 100%;
  display: flex;
  flex-direction: column;
  font-family: PingFangSC-Regular, PingFang SC;

  .container {
    width: 100%;
    height: 100%;

    .content{
      flex: 1;
      display: flex;
      height: calc(100vh - 88px);
      overflow: hidden;
      .main{
        flex: 1;
        height: 100%;
        overflow-y: auto;
      }
    }
  }
}
</style>
