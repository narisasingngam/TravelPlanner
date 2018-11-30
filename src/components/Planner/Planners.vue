<template>
    <v-container>
        <v-layout row wrap v-for="planner in planners" :key="planner.id" class="mb-2">
            <v-flex xs12 sm10 md8 offset-sm1 offset-md2>
                <v-card class="info">
                    <v-container fluid>
                        <v-layout row>
                            <v-flex xs5 sm4 md3>
                                <v-card-media
                                    :src="planner.imageUrl"
                                    height="130px"
                                >
                                </v-card-media>
                            </v-flex>
                            <v-flex xs7 sm8 md9>
                                <v-card-title primary-title>
                                    <div>
                                        <h2 class="white--text">{{ planner.topic}}</h2>
                                        <div>{{ planner.date }}</div>
                                    </div>
                                </v-card-title>
                                <v-card-action>
                                    <v-btn 
                                    @click="viewPlan"
                                    idlink = "planner.id"
      
                                    flat :to="'/planners/' + planner.id"
                                    >
                                        <v-icon left light>arrow_forward</v-icon>
                                        View planner</v-btn>
                                </v-card-action>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
            <v-flex xs3 sm10 md8 offset-sm1 offset-md2>
                <v-card
                    v-if="plannersIsValid"
                >
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">No planner</h3>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
            <v-flex xs3 sm10 md8 offset-sm1 offset-md2>
                <v-spacer></v-spacer>
                <v-btn
                class="error"
                v-if="userIsValid"
                @click="deletePlan"
                >
                    Delete
                </v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from "axios";
import { store } from "../../store";

export default {
  computed: {
    planners() {
      return this.$store.getters.loadedPlanners;
    },
    userIsValid() {
      return (
        this.$store.getters.getCookie("mail") == " " &&
        this.$store.getters.loadedPlanners.length > 0
      );
    },
    plannersIsValid() {
      return this.$store.getters.loadedPlanners.length == 0;
    }
  },

  mounted() {
    if (this.$store.getters.getCount == 0) {
      this.$store.dispatch("fetchUserData");
    }
    this.$store.commit("activeLoadedPlan", 1);
  },

  methods: {
    deletePlan() {
      this.$store.commit("clearPlanner");
      this.$log.info(`delete plan.`)
    }
  }
};
</script>
