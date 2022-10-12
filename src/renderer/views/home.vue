<template>
  <div class="main">
    <div class="left">

      <el-form ref="form" :model="form" :rules="rules" label-width="110px">
        <el-form-item label="迭代次数" prop="times">
          <el-input v-model="form.times"></el-input>
        </el-form-item>
        <el-form-item label="迭代间隔" prop="interval">
          <el-input v-model="form.interval"></el-input>
        </el-form-item>
        <el-form-item label="文件保存地址" prop="filePath">
          <el-input v-model="form.filePath"></el-input>
          <el-button type="primary" @click="onSelect" style="margin-top: 10px">选择文件保存地址</el-button>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="onStart">开始计算</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onUpdate">更新结果</el-button>
        </el-form-item>

        <el-form-item>
          运行过程提示: {{tips}}
        </el-form-item>
      </el-form>

    </div>
    <div class="right">
      <img :src="imgUrl" alt="">
    </div>
  </div>

</template>

<script>
import { ipcRenderer } from 'electron';

export default {
  name: 'home',
  data() {
    return {
      tips: '未开始',
      startCount: 0,
      form: {
        filePath: '/Users/wudong/Downloads/temp',
        times: 10,
        interval: 1,
      },
      rules: {
        times: [
          { required: true, message: '请输入迭代次数', trigger: 'blur' },
        ],
        interval: [
          { required: true, message: '请输入迭代间隔', trigger: 'change' },
        ],
        filePath: [
          { required: true, message: '请选择文件间隔', trigger: 'change' },
        ],
      },
      isStart: false,
      imgUrl: '',
    };
  },
  methods: {
    onSelect() {
      ipcRenderer.send('open-directory-dialog', 'openDirectory');

      ipcRenderer.once('selectFilePath', (e, file) => {
        this.form.filePath = file;
      });
    },

    onStart() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.isStart = true;
          this.startCount++;
          const { times, interval, filePath } = this.form;
          ipcRenderer.send('start', [this.startCount, times, interval, filePath]);

          ipcRenderer.once(`start_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
          });

          ipcRenderer.on(`stdout_${this.startCount}`, (event, data) => {
            console.log(event, data);
          });

          ipcRenderer.on(`stderr_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
          });

          ipcRenderer.once(`close_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
          });
        }
      });
    },

    onUpdate() {
      if (!this.isStart) {
        this.$message.warning('请先开始计算');
      }

      ipcRenderer.send('getResult', [this.form.filePath]);
      ipcRenderer.once('result', (event, data) => {
        console.log(event, data);
        this.imgUrl = data;
      });
    },
  },
};
</script>

<style scoped lang="less">
.main {
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
  padding: 24px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  .left {
    width: 500px;
    height: 100%;
    background: aquamarine;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .right {
    flex: 1;
    height: 100%;

    background: black;

    img {
      width: 100%;
      height: 100%;
      display: block;
    }
  }
}
</style>
