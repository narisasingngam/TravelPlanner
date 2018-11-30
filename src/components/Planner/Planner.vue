<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card>
          <v-card-title>
            <h1 class="primary--text">{{ planner.topic }}</h1>
          </v-card-title>
          <v-card-media :src="planner.imageUrl" height="400px"></v-card-media>
          <v-card-text>
            <div class="info--text">{{ planner.date }}</div>
          </v-card-text>
          <v-form>
            <v-layout align-center justify-center row class="pb-6">
              <v-flex xs2>
                <h4>Start Time</h4>
              </v-flex>
              <v-flex xs1>
                <v-combobox
                  v-model="selectStartTimeHour"
                  :items="hourList"
                  :disabled="this.disabled"
                ></v-combobox>
              </v-flex>
              <v-flex xs1>
                <h3>:</h3>
              </v-flex>
              <v-flex xs1>
                <v-combobox v-model="selectStartTimeMin" :items="minList" :disabled="this.disabled"></v-combobox>
              </v-flex>
            </v-layout>

            <v-layout align-center justify-center row class="pb-6">
              <v-flex xs2>
                <h4>End Time</h4>
              </v-flex>
              <v-flex xs1>
                <v-combobox v-model="selectEndTimeHour" :items="hourList" :disabled="this.disabled"></v-combobox>
              </v-flex>
              <v-flex xs1>
                <h3>:</h3>
              </v-flex>
              <v-flex xs1>
                <v-combobox v-model="selectEndTimeMin" :items="minList" :disabled="this.disabled"></v-combobox>
              </v-flex>
            </v-layout>

            <v-layout align-center justify-center row class="pb-6">
              <v-flex xs6 offset-xs2 offset-md2 offset-lg2>
                <vuetify-google-autocomplete
                  id="address"
                  append-icon="search"
                  ref="address"
                  :clearable="clearable"
                  :country="country"
                  :disabled="!dataIsValid"
                  :enable-="enableGeolocation"
                  label="Search Place"
                  prepend-icon="place"
                  required="true"
                  types="establishment"
                  onfocus="value = ''"
                  v-on:placechanged="getAddressData"
                  v-on:no-results-found="noResultsFound"
                ></vuetify-google-autocomplete>
              </v-flex>
            </v-layout>
            <v-layout align-center row class="pb-6">
              <v-flex xs3 offset-xs3 offset-md2>
                <h4>Spend time</h4>
              </v-flex>
              <v-flex xs1>
                <v-combobox v-model="spendTimeHour" :items="hourList"></v-combobox>
              </v-flex>
              <v-flex xs2>
                <h4>Hour(s)</h4>
              </v-flex>
              <v-flex xs1 offset-xs3 offset-md1>
                <v-combobox v-model="spendTimeMin" :items="minList"></v-combobox>
              </v-flex>
              <v-flex xs2>
                <h4>Minute(s)</h4>
              </v-flex>
            </v-layout>
          </v-form>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn class="primary" :disabled="!formIsValid" @click="addPlace">Add place</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-list two-line>
            <template v-for="(item, index) in list">
              <v-divider v-if="item.divider" :inset="item.inset" :key="index"></v-divider>
              <v-list-tile v-else-if="item.duration" :key="item.duration" avatar>
                <v-layout justify-center>
                  <v-list-action>
                    <v-icon>directions_car</v-icon>
                  </v-list-action>
                  <v-list-tile-content>
                    <v-list-tile-title>: {{ item.duration }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-layout>
              </v-list-tile>
              <v-list-tile v-else :key="item.name" avatar>
                <v-list-tile-avatar>
                  <img :src="item.avatar">
                </v-list-tile-avatar>
                <v-list-tile-content>
                  <v-list-tile-title v-html="item.name"></v-list-tile-title>
                  <v-list-tile-sub-title>Spend time: {{ item.spendtime }} hours</v-list-tile-sub-title>
                </v-list-tile-content>
                <v-list-tile-action>
                  <v-list-tile-action-text>Time: {{ item.time }}</v-list-tile-action-text>
                </v-list-tile-action>
              </v-list-tile>
            </template>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card>
          <v-card-actions>
            <v-spacer></v-spacer>
            <h2>Time remaining: {{ this.totalTime }} hours.minute</h2>
          </v-card-actions>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn class="error" @click="deletePlace" :disabled="!haveDATA">Delete</v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn class="primary" @click="alert = !alert" :disabled="!plannerIsValid">Save</v-btn>
          </v-card-actions>
          <v-card-text right>
            <v-spacer></v-spacer>
            <div class="info--text">If you want to save this plan, please sign in.</div>
          </v-card-text>
          <v-card-actions>
            <v-alert
              :value="alert"
              type="success"
              transition="scale-transition"
            >Do you want to save this planner?
              <v-btn @click.native.once="saveplan" class="info">OK</v-btn>
              <v-btn @click="alert = !alert" class="error">Close</v-btn>
            </v-alert>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import { store } from "../../store";
export default {
  data() {
    return {
      //auto-complete
      autocompleteModel: "Some Default Location...",
      vueGoogleAutocompleteLink:
        "https://github.com/olefirenko/vue-google-autocomplete",
      autocomplete: "",
      address: {},
      clearable: true,
      enableGeolocation: false,
      //data of place
      list: [],
      addressName: "",
      placeData: "0",
      placeList: [],
      saveList: [],
      //time data
      selectStartTimeHour: "00",
      selectStartTimeMin: "00",
      selectEndTimeHour: "00",
      selectEndTimeMin: "00",
      hourList: [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23"
      ],
      minList: [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
        "40",
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",
        "47",
        "48",
        "49",
        "50",
        "51",
        "52",
        "53",
        "54",
        "55",
        "56",
        "57",
        "58",
        "59"
      ],
      timePicker: "",
      totalTime: "",
      spendTimeHour: "00",
      spendTimeMin: "00",
      numSpendtime: "",
      totalmin: "",
      totalhour: "",
      disabled: false,
      numStartHour: "",
      numStartMin: "",
      alert: false,
      date: ""
    };
  },
  props: ["id"],
  created() {
    if (this.$store.getters.loadedPlanners.length == 0) {
      this.$store.dispatch("fetchUserData");
      this.$router.push("/planners");
    }
    this.$store.commit("activeLoadedPlan", 1);
  },
  mounted() {
    this.$store.dispatch(
      "dataPlanner",
      this.$store.getters.loadedPlanner(this.id).id
    );
  },
  computed: {
    planner() {
      if (
        this.$store.getters.getDataId ==
        this.$store.getters.loadedPlanner(this.id).id
      ) {
        console.log(this.$store.getters.getDataPlan);
        this.list = [];
        var count = 0;
        var size = this.$store.getters.getDataPlan.length;
        var data = this.$store.getters.getDataPlan;
        console.log(data[size - 1]["times"]);
        for (var i = 0; i < size - 1; i++) {
          if (i == 0) {
            this.list.push({
              avatar:
                "https://static1.squarespace.com/static/5572b7b4e4b0a20071d407d4/t/58a32d06d482e9d74eecebe4/1487751950104/Location+Based+Mobile-+Advertising",
              time: data[i]["times"],
              name: data[i]["location"],
              spendtime: data[i]["spendtime"],
              completed: false
            });
          } else {
            this.list.push(
              { divider: true, inset: true },
              { duration: data[i]["duration"] },
              { divider: true, inset: true },
              {
                avatar:
                  "https://static1.squarespace.com/static/5572b7b4e4b0a20071d407d4/t/58a32d06d482e9d74eecebe4/1487751950104/Location+Based+Mobile-+Advertising",
                time: data[i]["times"],
                name: data[i]["location"],
                spendtime: data[i]["spendtime"],
                completed: false
              }
            );
          }
        }
        this.totalTime = data[size - 1]["remaining"];
      }
      return this.$store.getters.loadedPlanner(this.id);
    },
    plannerIsValid() {
      return (
        this.list.length > 1 &&
        this.$store.getters.getCookie("mail") != " " &&
        this.$store.getters.getDataId !=
          this.$store.getters.loadedPlanner(this.id).id
      );
    },
    dataIsValid() {
      return (
        this.$store.getters.getDataId !=
        this.$store.getters.loadedPlanner(this.id).id
      );
    },
    formIsValid() {
      return (
        this.addressName != "" &&
        (this.spendTimeHour != "00" || this.spendTimeMin != "00") &&
        this.$store.getters.getDataId !=
          this.$store.getters.loadedPlanner(this.id).id
      );
    },
    outputJsData() {
      return `
                ${JSON.stringify(this.address)}
            `;
    },
    outputJsCallback() {
      return `methods: {
                ${
                  this.callbackFunction
                }: function (addressData, placeResultData) {
                this.address = addressData;
                }
            }`;
    },
    outputJs() {
      return `${this.outputJsData},
            ${this.outputJsCallback}`;
    },
    haveDATA() {
      return (
        this.list.length != 0 &&
        this.$store.getters.getDataId !=
          this.$store.getters.loadedPlanner(this.id).id
      );
    }
  },
  methods: {
    /**
     * Callback method when the location is found.
     *
     * @param {Object} addressData Data of the found location
     */
    getAddressData(addressData) {
      this.address = addressData;
      const addressStringify = JSON.stringify(this.address);
      const addressObj = JSON.parse(addressStringify);
      this.addressName = addressObj.name;
      // edok name tong nee
      console.log(this.addressName);
    },
    async addPlace() {
      // set time table
      this.setStartTime = `${this.selectStartTimeHour}:${
        this.selectStartTimeMin
      }`;
      // collect first place list
      this.placeList.push({ placeName: this.addressName });
      /** Show real total minute */
      const minDigit = function(totalmin) {
        if (totalmin < 10) return "0" + totalmin;
        return totalmin;
      };
      /** seperate hour and minute */
      const splitTimeTable = function(totalTime) {
        const splitTime = totalTime.split(".");
        return { hour: splitTime[0], min: splitTime[1] };
      };
      const plusTime = function(startHour, startMin, endHour, endMin) {
        let min = 0;
        let hour = 0;
        if (startMin + endMin > 60) {
          min = startMin + endMin - 60;
          hour = startHour + endHour + 1;
        } else {
          min = startMin + endMin;
          hour = startHour + endHour;
        }
        return { hour: minDigit(hour), min: minDigit(min) };
      };
      /** Compute time table */
      const timeTable = function(
        selectEndTimeHour,
        selectEndTimeMin,
        selectStartTimeHour,
        selectStartTimeMin
      ) {
        const startTimefirst = new Date(
          `Jan 1, 2018 ${selectStartTimeHour}:${selectStartTimeMin}:00`
        );
        const endTimefirst = new Date(
          `Jan 1, 2018 ${selectEndTimeHour}:${selectEndTimeMin}:00`
        );
        const endTimenext = new Date(
          `Jan 2, 2018 ${selectEndTimeHour}:${selectEndTimeMin}:00`
        );
        let date1;
        let date2;
        if (selectStartTimeHour < selectEndTimeHour) {
          date1 = startTimefirst;
          date2 = endTimefirst;
        } else if (selectStartTimeHour == selectEndTimeHour) {
          if (selectStartTimeMin == selectEndTimeMin) {
            return { totalhour: 24, totalmin: 0 };
          } else if (selectStartTimeMin < selectEndTimeMin) {
            date1 = startTimefirst;
            date2 = endTimefirst;
          } else {
            date1 = startTimefirst;
            date2 = endTimenext;
          }
        } else {
          date1 = startTimefirst;
          date2 = endTimenext;
        }
        const res = Math.abs(date1 - date2) / 1000;
        // get hours
        const hours = Math.floor(res / 3600) % 24;
        // get minutes
        const minutes = Math.floor(res / 60) % 60;
        return { totalhour: hours, totalmin: minDigit(minutes) };
      };
      let splitTimeDuration = function(placeData) {
        var splitDuration = placeData.split(" ");
        if (
          splitDuration[1] === "hour" ||
          (splitDuration[1] === "hours" && splitDuration[3] === "mins") ||
          splitDuration[3] === "min"
        ) {
          return {
            hour: parseInt(splitDuration[0], 10),
            min: parseInt(splitDuration[2], 10)
          };
        } else if (
          splitDuration[1] === "hour" ||
          splitDuration[1] === "hours"
        ) {
          return { hour: parseInt(splitDuration[0], 10), min: 0 };
        } else if (splitDuration[1] === "mins" || splitDuration[1] === "min") {
          return { hour: 0, min: parseInt(splitDuration[0], 10) };
        }
        return { hour: 0, min: 0 };
      };
      if (this.list.length >= 1) {
        let placeOrigin = this.placeList.length - 2;
        let placeDestination = this.placeList.length - 1;
        try {
          let bodyPlace = {
            place: this.placeList[placeDestination].placeName,
            origin: this.placeList[placeOrigin].placeName
          };
          let placeResponse = await axios.post(
            process.env.PLACE_DURATION,
            bodyPlace
          );
          this.placeData = placeResponse.data;
          console.log(placeResponse.data);
        } catch (error) {
          this.$log.error(error);
          // dont forget to subtract time remain
          alert(
            "These two places maybe too far or don't have in the map. Please select new places."
          );

          this.placeList.pop();
          this.$refs.address.clear();
          return;
        }
        // plus time table
        let num = plusTime(
          parseInt(this.numStartHour, 10),
          parseInt(this.numStartMin, 10),
          splitTimeDuration(this.placeData).hour,
          splitTimeDuration(this.placeData).min
        );
        let num1 = plusTime(
          parseInt(num.hour, 10),
          parseInt(num.min, 10),
          parseInt(this.numSpendtimeHour, 10),
          parseInt(this.numSpendtimeMin, 10)
        );
        this.numStartHour = num1.hour;
        this.numStartMin = num1.min;
        this.numSpendtimeHour = this.spendTimeHour;
        this.numSpendtimeMin = this.spendTimeMin;
        this.spendtime =
          parseInt(this.spendTimeHour, 10) + "." + this.spendTimeMin;
        this.timePicker = this.numStartHour + ":" + this.numStartMin;
        this.list.push(
          { divider: true, inset: true },
          { duration: this.placeData },
          { divider: true, inset: true },
          {
            avatar:
              "https://static1.squarespace.com/static/5572b7b4e4b0a20071d407d4/t/58a32d06d482e9d74eecebe4/1487751950104/Location+Based+Mobile-+Advertising",
            time: this.timePicker,
            name: this.addressName,
            spendtime: this.spendtime,
            completed: false
          }
        );
        this.saveList.push({
          email: this.$store.getters.getCookie("mail"),
          location: this.addressName,
          spendtime: this.spendtime,
          times: this.timePicker,
          date: this.$store.getters.loadedPlanner(this.id).date,
          id: this.$store.getters.loadedPlanner(this.id).id,
          name: this.$store.getters.loadedPlanner(this.id).topic,
          duration: this.placeData,
          remaining: this.totalTime
        });
      } else {
        try {
          let bodyAddress = {
            place: this.addressName
          };
          let addressResponse = await axios.post(
            process.env.SEARCH,
            bodyAddress
          );
        } catch (error) {
          this.$log.error(error);
          alert(
            "This place maybe doesn't have in the map. Please select new places."
          );
          this.$refs.address.clear();
          return;
        }
        this.numStartHour = this.selectStartTimeHour;
        this.numStartMin = this.selectStartTimeMin;
        this.numSpendtimeHour = this.spendTimeHour;
        this.numSpendtimeMin = this.spendTimeMin;
        this.spendtime =
          parseInt(this.spendTimeHour, 10) + "." + this.spendTimeMin;
        this.totalTime =
          timeTable(
            this.selectEndTimeHour,
            this.selectEndTimeMin,
            this.selectStartTimeHour,
            this.selectStartTimeMin
          ).totalhour +
          "." +
          timeTable(
            this.selectEndTimeHour,
            this.selectEndTimeMin,
            this.selectStartTimeHour,
            this.selectStartTimeMin
          ).totalmin;
        this.list.push({
          avatar:
            "https://static1.squarespace.com/static/5572b7b4e4b0a20071d407d4/t/58a32d06d482e9d74eecebe4/1487751950104/Location+Based+Mobile-+Advertising",
          time: this.setStartTime,
          name: this.addressName,
          spendtime: this.spendtime,
          completed: false
        });
        this.disabled = true;
        this.saveList.push({
          email: this.$store.getters.getCookie("mail"),
          location: this.addressName,
          spendtime: this.spendtime,
          times: this.setStartTime,
          date: this.$store.getters.loadedPlanner(this.id).date,
          id: this.$store.getters.loadedPlanner(this.id).id,
          name: this.$store.getters.loadedPlanner(this.id).topic,
          duration: "0",
          remaining: this.totalTime
        });
      }
      let size = this.list.length - 1;
      try {
        let bodyTime = {
          spendtime: this.list[size].spendtime,
          remaining: this.totalTime,
          road: this.placeData
        };
        let timeResponse = await axios.post(process.env.TIME_REMAIN, bodyTime);
        if (timeResponse.data < 0) {
          alert("Your time is over date");
          this.list.splice(this.list.length - 3, 4);
          this.placeList.pop();
          this.saveList.pop();
          timeResponse.data = this.totalTime;
        }
        this.totalTime = timeResponse.data;
        console.log(timeResponse.data);
      } catch (error) {
        this.$log.error(error);
      }
      this.addressName = "";
      this.$refs.address.clear();
      this.address = "";
      this.spendtime = "";
    },
    deletePlace() {
      console.log("remove");
      console.log(this.list.length);
      console.log(this.saveList);
      var removeP = this.saveList[this.saveList.length - 1]["location"];
      this.$log.info(`remove ${removeP}`);
      this.totalTime = this.saveList[this.saveList.length - 1]["remaining"];

      if (this.list.length <= 4) this.list.splice(0, 4);
      else this.list.splice(this.list.length - 3, 4);
      this.saveList.pop();
      this.placeList.pop();
    },
    async saveplan() {
      this.saveList.push({
        email: this.$store.getters.getCookie("mail"),
        location: this.addressName,
        spendtime: this.spendtime,
        times: this.setStartTime,
        date: this.$store.getters.loadedPlanner(this.id).date,
        id: this.$store.getters.loadedPlanner(this.id).id,
        name: this.$store.getters.loadedPlanner(this.id).topic,
        duration: this.placeData,
        remaining: this.totalTime
      });
      try {
        for (const i of this.saveList) {
          console.log(i);
          let save = await axios.post(process.env.SAVE_DATA, i);
          console.log(save.data);
          this.$log.info(`${i} saved!`);
        }
        alert("Save succesful!");
      } catch (error) {
        this.$log.error(error);
      }
    }
  }
};
</script>

