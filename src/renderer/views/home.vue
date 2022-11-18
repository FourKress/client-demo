<template>
  <div class="main">
    <el-tabs type="border-card" class="tabs">
      <el-tab-pane label="用户管理">用户管理</el-tab-pane>
      <el-tab-pane label="配置管理">配置管理</el-tab-pane>
      <el-tab-pane label="角色管理">角色管理</el-tab-pane>
      <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
    </el-tabs>
<!--    <div class="left">-->
<!--      <el-form ref="form" :model="form" :rules="rules" label-width="110px">-->
<!--        <el-form-item label="迭代次数" prop="count">-->
<!--          <el-input v-model="form.count"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="迭代时间" prop="time">-->
<!--          <el-input v-model="form.time"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="文件保存地址" prop="filePath">-->
<!--          <el-input v-model="form.filePath"></el-input>-->
<!--          <el-button type="primary" @click="onSelect" style="margin-top: 10px"-->
<!--            >选择文件保存地址</el-button-->
<!--          >-->
<!--        </el-form-item>-->

<!--        <el-form-item>-->
<!--          <el-button type="primary" @click="onStart" :disabled="isStart"-->
<!--            >开始计算</el-button-->
<!--          >-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button type="primary" @click="onUpdate" :disabled="!isResult"-->
<!--            >更新结果</el-button-->
<!--          >-->
<!--        </el-form-item>-->

<!--        <el-form-item> 运行过程提示: {{ tips }} </el-form-item>-->
<!--      </el-form>-->
<!--    </div>-->
<!--    <div class="right">-->
<!--      <img :src="imgUrl" alt="" />-->
<!--    </div>-->
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
        time: 5,
        count: 10,
      },
      rules: {
        count: [{ required: true, message: '请输入迭代次数', trigger: 'blur' }],
        time: [
          { required: true, message: '请输入迭代时间', trigger: 'change' },
        ],
        filePath: [
          { required: true, message: '请选择文件保存地址', trigger: 'change' },
        ],
      },
      isStart: false,
      isResult: false,
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
          this.isResult = false;
          this.startCount++;
          const { count, time, filePath } = this.form;
          ipcRenderer.send('start', [
            this.startCount,
            {
              count,
              time,
              filePath,
            },
          ]);

          ipcRenderer.once(`start_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
          });

          ipcRenderer.on(`stdout_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.isResult = true;
          });

          ipcRenderer.on(`stderr_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
          });

          ipcRenderer.once(`close_${this.startCount}`, (event, data) => {
            console.log(event, data);
            this.tips = data;
            this.isStart = false;
          });
        }
      });
    },

    onUpdate() {
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
  width: 100%;
  height: 100%;
  box-sizing: border-box;

  .tabs {
  }
}
</style>
