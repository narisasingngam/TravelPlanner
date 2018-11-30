<template>
   <v-app>
        <v-container>
            <v-layout row>
                <v-flex xs12 sm6 offset-sm3>
                    <h1 class="primary--text">Create a new planner</h1>
                </v-flex>
            </v-layout>
            <v-space></v-space>
            <v-layout align-center justify-center row>
                <v-flex xs12>
                    <v-form @submit.prevent="onCreatePlanner">
                        <v-layout row>
                            <v-flex xs12 sm6 offset-sm3>
                                <v-text-field
                                    name="topic"
                                    label="Topic"
                                    id="topic"
                                    v-model="topic"
                                    required></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout row class="mb-6">
                            <v-flex xs12 sm6 offset-sm3>
                                <h2 class="grey--text">Choose a date</h2>
                            </v-flex>
                        </v-layout>
                        <v-layout align-center justify-center row >
                            <v-flex xs12 sm6>
                                <v-menu
                                    ref="menu"
                                    :close-on-content-click="false"
                                    v-model="menu"
                                    :nudge-right="40"
                                    lazy
                                    transition="scale-transition"
                                    offset-y
                                    full-width
                                    max-width="290px"
                                    min-width="290px"
                                    >
                                    <v-text-field
                                        slot="activator"
                                        v-model="dateFormatted"
                                        label="Date"
                                        hint="MM/DD/YYYY format"
                                        persistent-hint
                                        prepend-icon="event"
                                        @blur="date = parseDate(dateFormatted)"
                                    ></v-text-field>
                                    <v-date-picker v-model="date" no-title @input="menu = false"></v-date-picker>
                                </v-menu>
                            </v-flex>
                        </v-layout>
                        <v-layout align-center justify-center row>
                            <v-flex xs1 class="mb-6">
                                <v-btn
                                class="primary"
                                :disabled="!formIsValid"

                                type="submit">Create planner</v-btn>
                            </v-flex>
                        </v-layout>
                        <v-layout align-center justify-center row wrap>
                            <v-flex xs5 class="mb-6">
                                <v-card-text right>
                                    <div class="info--text">If you want to create many plan, please sign in.</div>
                                </v-card-text>
                            </v-flex>
                        </v-layout>
                    </v-form>
                </v-flex>
            </v-layout>
        </v-container>
   </v-app>
</template>

<script>
import axios from "axios";
import { store } from "../../store";

export default {
  data() {
    return {
      topic: "",
      imageUrl:
        "https://wp-assets.dotproperty-kh.com/wp-content/uploads/sites/14/2016/10/28150318/Fotolia_116473721_Subscription_Monthly_M.jpg",
      date: null,
      dateFormatted: null,
      menu: false,
      picker: null,
      landscape: false
    };
  },
  computed: {
    formIsValid() {
      if (this.$store.getters.getCookie("mail") == " ") {
        return (
          this.$store.getters.loadedPlanners.length == 0 &&
          this.topic !== "" &&
          this.date !== null
        );
      }
      return this.topic !== "" && this.date !== null;
    },
    computedDateFormatted() {
      return this.formatDate(this.date);
    }
  },
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    }
  },

  methods: {
    onCreatePlanner() {
      if (!this.formIsValid) {
        return;
      }
      this.$store.commit("setIdPlan");
      const plannerData = {
        imageUrl: this.imageUrl,
        topic: this.topic,
        date: this.date,
        id: this.$store.getters.getId
      };
      this.$store.dispatch("createPlanner", plannerData);
      this.$router.push("/planners");
      this.$log.info(`create planner name: ${this.topic}, date: ${this.date}`)
    },

    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");

      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    }
  }
};
</script>


<style lang="stylus">
</style>
