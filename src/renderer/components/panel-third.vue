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
        <el-form-item label="选择工作目录" prop="parameters_turbine">
          <el-button type="primary" @click="onSelectOnly('parameters_turbine')">
            选择
          </el-button>
          <el-tag
            v-if="form.parameters_turbine"
            closable
            @close="handlePathCloseOnly('parameters_turbine')"
          >
            {{ form.parameters_turbine }}
          </el-tag>
        </el-form-item>

        <el-form-item label="num_opt_iteration" prop="num_opt_iteration">
          <el-input v-model="form.num_opt_iteration"></el-input>
        </el-form-item>
        <el-form-item label="step_check" prop="step_check">
          <el-input v-model="form.step_check"></el-input>
        </el-form-item>
        <el-form-item label="name_to_save" prop="name_to_save">
          <el-input v-model="form.name_to_save"></el-input>
        </el-form-item>
        <el-form-item label="name_to_load" prop="name_to_load">
          <el-input v-model="form.name_to_load"></el-input>
        </el-form-item>
      </div>
      <div class="right">
        <el-form-item
          label="高级选项"
          prop="is_specify_loc_turbines_initial"
        >
          <el-checkbox
            v-model="form.is_specify_loc_turbines_initial"
          ></el-checkbox>
        </el-form-item>

        <el-form-item
          label="is_set_new_vel"
          prop="is_set_new_vel"
        >
          <el-checkbox
            :disabled="!form.is_specify_loc_turbines_initial"
            v-model="form.is_set_new_vel"
          ></el-checkbox>
        </el-form-item>
        <el-form-item
          label="is_new_flow_field"
          prop="is_new_flow_field"
        >
          <el-checkbox
            :disabled="!form.is_specify_loc_turbines_initial"
            v-model="form.is_new_flow_field"
          ></el-checkbox>
        </el-form-item>

        <el-form-item label="seed_numpy" prop="seed_numpy">
          <el-input :disabled="!form.is_specify_loc_turbines_initial" v-model="form.seed_numpy"></el-input>
        </el-form-item>
        <el-form-item label="num_particles" prop="num_particles">
          <el-input :disabled="!form.is_specify_loc_turbines_initial" v-model="form.num_particles"></el-input>
        </el-form-item>
        <el-form-item label="fitness_initial" prop="fitness_initial">
          <el-input :disabled="!form.is_specify_loc_turbines_initial" v-model="form.fitness_initial"></el-input>
        </el-form-item>
      </div>
    </el-form>

    <div class="btn-list">
      <el-button type="primary" @click="onStart" class="save-btn">
        新计算
      </el-button>
      <el-button type="primary" @click="onContinue" class="save-btn">
        继续计算
      </el-button>
    </div>
  </div>
</template>

<script>
import Mixins from '../mixins';

export default {
  name: 'PanelFirst',
  mixins: [Mixins],
  data() {
    return {
      form: {
        parameters_turbine: '',
        num_opt_iteration: '',
        step_check: '',
        name_to_save: '',
        name_to_load: '',
        is_specify_loc_turbines_initial: false,
        is_set_new_vel: false,
        is_new_flow_field: false,
        seed_numpy: '',
        num_particles: '',
        fitness_initial: '',
      },
      rules: {
        parameters_turbine: [
          { required: true, message: '请选择', trigger: ['blur', 'change'] },
        ],
        num_opt_iteration: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
        step_check: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
        name_to_save: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
        name_to_load: [
          { required: true, message: '请输入', trigger: ['blur', 'change'] },
        ],
      },
    };
  },
  methods: {
    validate() {
      return new Promise((resolve) => {
        this.$refs.form.validate((valid) => {
          resolve(valid);
        });
      });
    },

    onContinue() {
      this.$emit('start', true);
    },
    onStart() {
      this.$emit('start', false);
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
    width: 600px;
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

.btn-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.save-btn {
  width: 120px;
  display: block;
}
</style>
