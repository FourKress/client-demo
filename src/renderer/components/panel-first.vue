<template>
  <div class="tab-panel">
    <el-form
      class="form-panel"
      ref="form"
      :model="form"
      :rules="rules"
      label-width="150px"
    >
      <div class="left">
        <el-form-item label="parameters_turbine" prop="parameters_turbine">
          <el-button
            type="primary"
            :disabled="isStart || true"
            @click="onSelect('parameters_turbine')"
          >
            选择
          </el-button>
          <div class="tag-panel" v-if="form.parameters_turbine.length">
            <el-tag
              v-for="path in form.parameters_turbine"
              :key="path"
              :closable="!isStart"
              @close="handlePathClose(path, 'parameters_turbine')"
            >
              {{ path }}
            </el-tag>
          </div>
        </el-form-item>

        <el-form-item label="num_turbines" prop="num_turbines">
          <el-input :disabled="isStart" v-model="form.num_turbines"></el-input>
        </el-form-item>
        <el-form-item label="dist_threshold" prop="dist_threshold">
          <el-input
            :disabled="isStart"
            v-model="form.dist_threshold"
          ></el-input>
        </el-form-item>
        <el-form-item label="height_hub" prop="height_hub">
          <el-input :disabled="isStart" v-model="form.height_hub"></el-input>
        </el-form-item>
      </div>
      <div class="right">
        <el-form-item
          label="is_specify_loc_turbines_initial"
          prop="is_specify_loc_turbines_initial"
          label-width="200px"
        >
          <el-checkbox
            :disabled="isStart"
            v-model="form.is_specify_loc_turbines_initial"
          ></el-checkbox>
        </el-form-item>

        <el-form-item
          label="dir_turbine_loc"
          prop="dir_turbine_loc"
          label-width="200px"
          :rules="[
            {
              required: form.is_specify_loc_turbines_initial,
              message: '请选择',
              trigger: ['blur', 'change'],
            },
          ]"
        >
          <el-button
            type="primary"
            :disabled="isStart || !form.is_specify_loc_turbines_initial"
            @click="onSelectOnly('dir_turbine_loc')"
          >
            选择
          </el-button>

          <el-tag
            v-if="form.dir_turbine_loc"
            :closable="!isStart"
            @close="handlePathCloseOnly('dir_turbine_loc')"
          >
            {{ form.dir_turbine_loc }}
          </el-tag>
        </el-form-item>
      </div>
    </el-form>
  </div>
</template>

<script>
import Mixins from '../mixins';

export default {
  name: 'PanelFirst',
  mixins: [Mixins],
  props: ['isStart'],
  data() {
    return {
      form: {
        parameters_turbine: [],
        num_turbines: '',
        dist_threshold: '',
        height_hub: '',
        is_specify_loc_turbines_initial: false,
        dir_turbine_loc: '',
      },
      rules: {
        // parameters_turbine: [
        //   { required: true, message: '请选择', trigger: ['blur', 'change'] },
        // ],
        num_turbines: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
        dist_threshold: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
        height_hub: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
      },
    };
  },
  methods: {
    validate() {
      return new Promise((resolve) => {
        this.$refs.form.validate((valid) => {
          resolve({
            valid,
            form: {
              ...this.form,
              parameters_turbine: undefined,
            },
          });
        });
      });
    },
  },
};
</script>

<style scoped lang="less">
.tab-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.form-panel {
  flex: 1;
  display: flex;
  align-items: flex-start;

  .left,
  .right {
    width: 800px;
  }

  .tag-panel {
    width: 100%;
    max-height: 150px;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 6px 12px;
    border: 1px solid #ccc;
    margin-top: 8px;
    box-sizing: border-box;
  }

  .el-tag {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 6px 0;
  }

  .left {
    margin-right: 48px;
  }
}
</style>
