<template>

 <div v-if="usname == ' ' || usname == '' || usname == null">
  <v-container>
   <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
       <!-- layout for signin -->
      <v-card>
         <v-card-media
          src="http://www.dream-wallpaper.com/free-wallpaper/travel-wallpaper/santorini-wallpaper/1680x1050/free-wallpaper-18.jpg"
          aspect-ratio="2.75"
        ></v-card-media>
        <v-card-title primary-title>
          <div>
            <h1 class="headline mb-0">Sign in</h1>
          </div>
        </v-card-title>
        <v-layout row>
          <v-flex xs1 offset-xs3 offset-md2 offset-lg2>
            <v-card-media
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2000px-Google_%22G%22_Logo.svg.png"
              aspect-ratio="1"
              height="50px"
              width="50px"
              ></v-card-media>
          </v-flex>
          <v-card-actions >
          <v-layout row>
            <v-flex s1 offset-xs3 >
               <v-btn @click="signIn" :disabled="!isLoaded" class="info">sign in</v-btn>
            </v-flex>
          </v-layout>
        </v-card-actions>
        </v-layout>
      </v-card>
    </v-flex>
   </v-layout>
  </v-container>
</div>

<div v-else>
 <v-container>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
 <!-- sign out -->
      <v-card>
        <v-card-media
          src="http://www.dream-wallpaper.com/free-wallpaper/travel-wallpaper/santorini-wallpaper/1680x1050/free-wallpaper-18.jpg"
          aspect-ratio="2.75"
        ></v-card-media>
         <v-card-title primary-title>
          <div>
            <h1 class="headline mb-0">Account</h1>
          </div>
        </v-card-title>
        <v-flex offset-xs3 offset-md2 offset-lg2>
          <h2> name: {{usname}} </h2>
          <h2> email: {{email}}</h2>
        </v-flex>
        <v-card-actions >
          <v-layout row>
            <v-flex s1 offset-xs3 >
               <v-btn @click="signOut" :disabled="!isLoaded" class="secondary">sign out</v-btn>
            </v-flex>
          </v-layout>
        </v-card-actions>
      </v-card>
     </v-flex>
   </v-layout>
  </v-container>
</div>
</template>


<script>
import { store } from "../../store";

export default {
  name: "SignIn",
  nameUser: true,
  store,
  data() {
    return {
      isLoaded: false,
      user: {
        username: " ",
        email: " "
      }
    };
  },
  methods: {
    signIn() {
      this.$gAuth
        .signIn()
        .then(user => {
          this.$store.commit("setUsername", user.w3.ig);
          this.$store.commit("setEmail", user.w3.U3);

          let us = user["w3"]["ig"];
          let ml = user["w3"]["U3"];

          this.$store.getters.Cookie("name", us);
          this.$store.getters.Cookie("mail", ml);

          this.$store.commit(
            "setUsername",
            this.$store.getters.getCookie("name")
          );
          this.$store.commit("setEmail", this.$store.getters.getCookie("mail"));

          this.user.username = this.$store.getters.getCookie("name");
          this.user.email = this.$store.getters.getCookie("mail");
          this.$store.commit("clearPlanner");
          if (this.$store.getters.getCookie("mail") != " ") {
            this.$store.dispatch("fetchUserData");
          }
          this.$log.info(this.user.username);
          this.$log.info(this.user.email);
        })
        .catch(error => {
          this.$log.error(error);
        });
    },
    signOut() {
      this.$gAuth
        .signOut()
        .then(user => {
          this.$store.getters.Cookie("name", " ");
          this.$store.getters.Cookie("mail", " ");

          this.$store.commit(
            "setUsername",
            this.$store.getters.getCookie("name")
          );
          this.$store.commit("setEmail", this.$store.getters.getCookie("mail"));

          this.user.username = this.$store.getters.getCookie("name");
          this.user.email = this.$store.getters.getCookie("mail");
          this.$store.commit("clearPlanner");

          this.$log.info(`${this.user.username} sign out.`);
        })
        .catch(error => {
          this.$log.error(error);
        });
    }
  },
  computed: {
    usname() {
      // console.log(this.$store.getters.getCookie('name'))
      this.user.username = this.$store.getters.getCookie("name");
      return this.user.username;
    },
    email() {
      // console.log(this.$store.getters.getCookie('mail'))
      this.user.email = this.$store.getters.getCookie("mail");
      return this.user.email;
    }
  },
  mounted() {
    const that = this;
    const checkGauthLoad = setInterval(() => {
      that.isLoaded = that.$gAuth.isLoaded();
      if (that.isLoaded) clearInterval(checkGauthLoad);
    }, 1000);
  }
};
</script>

<style>
.g-signin-button {
  /* This is where you control how the button looks. Be creative! */
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  /* box-shadow: 0 3px 0 #0f69ff; */
}
.fb-signin-button {
  /* This is where you control how the button looks. Be creative! */
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #4267b2;
  color: #fff;
}
</style>
