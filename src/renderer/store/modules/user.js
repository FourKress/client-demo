/**
 * 用户信息持久化
 * @type {{userInfo: {}, userInfoError: {visible: boolean, message: string}}}
 */

const state = {
  userInfo: {},
  userMenu: [],
  authBtn: [],
  userInfoError: {
    visible: false,
    message: '',
    type: '',
  },
  userInfoErrorCode: undefined,
};

const getters = {
  userInfo(data) {
    return data.userInfo;
  },
  userMenu(data) {
    return data.userMenu;
  },
  authBtn(data) {
    return data.authBtn;
  },
  userInfoError(data) {
    return data.userInfoError;
  },
  userInfoErrorCode(state) {
    return state.userInfoErrorCode;
  },
};

const mutations = {
  updateUserInfo(data, value) {
    const { user, resources } = value || {};
    data.userInfo = user;
    data.userMenu = resources;
  },
  updateAuthBtn(data, value) {
    data.authBtn = value;
  },
  clearUserInfo(data) {
    data.userInfo = {};
  },
  userInfoError(data, value) {
    data.userInfoError = value;
  },
  setUserInfoErrorCode(state, value) {
    state.userInfoErrorCode = value;
  },
};

const actions = {
  setUserInfoErrorCode({ commit }, value) {
    commit('setUserInfoErrorCode', value);
  },
  updateUserInfo({ commit }, value) {
    commit('updateUserInfo', value);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
