import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { stat } from 'fs';
import VueCookie from 'vue-cookies';

Vue.use(Vuex);
Vue.use(VueCookie);

export const store = new Vuex.Store({
    state: {
        loadedPlanners: [],
        listId: [],
        user: {
            username: ' ',
            email: ' ',
        },
        planUser: [],

        idPlan: '01',
        dataId: ' ',
        listData: [],
        count: 0,
        planner: [],
    },
    mutations: {
        createPlanner(state, payload) {
            state.loadedPlanners.push(payload);
        },
        setUsername(state, name) {
            state.user.username = name;
        },
        setEmail(state, email) {
            state.user.email = email;
        },
        clearPlanner(state) {
            state.loadedPlanners = [];
        },
        setIdPlan(state) {
            state.idPlan = Math.random().toString(36).substr(2, 9);
        },
        activeLoadedPlan(state, numcount) {
            state.count = numcount
        },
        dataPlan(state, plan) {
            state.planUser = plan;
        },
        setDataId(state, id) {
            state.dataId = id;
        },
        addListData(state, listdata) {
            state.listData.push = listdata
        },
        addPlan(state, payload) {
            state.planner.push(payload)
        },
        addDivide(state, payload) {
            state.planner.push(payload)
        },
        addDuration(state, payload) {
            state.planner.push(payload)
        },
        setIdPlan(state) {
            state.idPlan = Math.random().toString(36).substr(2, 9);
        }

    },
    actions: {

        async dataPlanner({ commit, getters }, idplan) {
            if (getters.getCookie("mail") != " ") {
                const bodyUser = {
                    email: getters.getCookie("mail"),
                    id: idplan
                }

                try {

                    const planData = await axios.post(process.env.PLAN_DATA, bodyUser);
                    console.log(planData.data)
                    console.log(planData.data[0]['id'])
                    commit('setDataId', planData.data[0]['id'])
                    commit('dataPlan', planData.data);


                } catch (error) {
                    this.$log.error(error);
                    return 0;
                }
            }
        },

        async fetchUserData({ commit, getters }) {
            console.log(getters.getCookie("mail"));
            if (getters.getCookie("mail") != " ") {

                const bodyUser = {
                    email: getters.getCookie("mail"),
                };
                try {

                    const userDate = await axios.post(
                        process.env.USER_DATA,
                        bodyUser,
                    );

                    console.log(userDate.data);

                    for (let i = 0; i < userDate.data.length; i++) {
                        const UserData = {
                            topic: userDate.data[i]['name'],
                            imageUrl:
                                'https://wp-assets.dotproperty-kh.com/wp-content/uploads/sites/14/2016/10/28150318/Fotolia_116473721_Subscription_Monthly_M.jpg',
                            date: userDate.data[i]['date'],
                            id: userDate.data[i]['id'],
                        };
                        commit('addListData', userDate.data[i]['id']);
                        commit('createPlanner', UserData);
                        // console.log(getters.loadedPlanners);

                    }
                } catch (error) {
                    this.$log.error(error);
                    return;
                }
            }
        },

        createPlanner({ commit }, payload) {
            const planner = {
                imageUrl: payload.imageUrl,
                id: payload.id,
                topic: payload.topic,
                date: payload.date,
            };
            // Reach out to database and store it
            commit('createPlanner', planner);
        },
        addDuration({ commit }, payload) {
            const placeDuration = { duration: payload.duration }
            commit('addDuration', placeDuration);
        },
        addDivide({ commit }, payload) {
            const divide = { divider: true, inset: true };
            commit('addDivide', divide);
        },
        addPlan({ commit }, payload) {
            const placeList = ({
                avatar: 'https://static1.squarespace.com/static/5572b7b4e4b0a20071d407d4/t/58a32d06d482e9d74eecebe4/1487751950104/Location+Based+Mobile-+Advertising',
                time: payload.time,
                name: payload.name,
                spendtime: payload.spendtime,
                completed: false,
            })

            commit('addPlan', placeList)
        },

        username(state, name) {
            state.commit('setUsername', name);
        },
        email(state, email) {
            state.commit('setEmail', email);
        },
        clearCreatePlanner(state) {
            state.commit('clearCreatePlanner');
        },


    },
    getters: {
        getPlan(state) {
            return state.planner
        },
        loadedPlanners(state) {
            return state.loadedPlanners.sort((plannerA, plannerB) => plannerA.date > plannerB.date);
        },
        featuredPlanners(state, getters) {
            return getters.loadedPlanners.slice(0, 5);
        },
        loadedPlanner(state) {
            return (plannerId) => {
                return state.loadedPlanners.find((planner) => {
                    return planner.id === plannerId
                })
            }
        },

        getUsername: state => state.user.username,
        getEmail: state => state.user.email,
        // genarate id
        getId: state => state.idPlan,
        //Id from database
        getDataId: state => state.dataId,
        getDataPlan: state => state.planUser,
        getListData: state => state.listData,

        getId: state => state.idPlan,

        getCookie: state => key => Vue.cookie.get(key),
        Cookie: state => (key, value) => Vue.cookie.set(key, value, '1h'),
        getCount: state => state.count
    }


});
