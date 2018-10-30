<template>
  <v-container>
    <v-layout row>
            <v-flex xs12>
                <input type="text" class="place-input" placeholder="where do you want to go?" v-model="newPlace"
                @keyup.enter="addPlace">
            </v-flex>
        </v-layout>
  </v-container>
</template>

<script>
export default {
    data () {
      return {
        place: '',
        time: '',
        duration: '',
        newPlace: '',
      }
    },
    method: {
        addPlace() {
            // this.list.push({
            //     time: this.time,
            //     name: this.place,
            //     timeDuration: this.duration,
            //     completed: false,
            // })
            // this.timeDuration = ''
            alert('addPlace')
        },
    },
}
</script>

