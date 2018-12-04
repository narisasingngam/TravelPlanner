<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12 sm6 class="text-xs-center text-sm-right mb-6">
                <v-btn large router to="/planners" class="primary">Explore Planners</v-btn>
            </v-flex>
            <v-flex xs12 sm6 class="text-xs-center text-sm-right mb-6">
                <v-btn large router to="/planner/new" class="primary">Organize Planners</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
           <v-carousel>
                <v-carousel-item
                v-for="planner in planners"
                :key="planner.id"
                :src="planner.imageUrl"
                @click="onLoadPlanner(planner.id)">
                <div class="title">
                    {{ planner.topic }}
                </div>
                </v-carousel-item>
                </v-carousel>
        </v-layout>
    </v-container>
</template>

<script>
import { store } from "../store";
export default {

  computed: {
    planners() {
        if (this.$store.getters.loadedPlanners.length == 0) {
            console.log("in")
            return [{
                topic: "Welcome to Travel planner",
                imageUrl: require('../assets/travel-planner.png'),
            }]
        }
      return this.$store.getters.featuredPlanners;
    }
  },

  methods: {
    onLoadPlanner(id) {
      this.$router.push(/planners/ + id);
    }
  }
};
</script>
