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
                    <v-form>
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
                        <v-layout row>
                            <v-flex xs12 sm6 offset-sm3>
                                <v-text-field
                                    name="imageURL"
                                    label="imageURL"
                                    id="image-url"
                                    v-model="imageURL"
                                    required></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout row>
                            <v-flex xs12 sm6 offset-sm3>
                                <img :src="imageURL" height="150">
                            </v-flex>
                        </v-layout>
                        <v-layout row class="mb-6">
                            <v-flex xs12 sm6 offset-sm3>
                                <h2 class="grey--text">Choose a date and time</h2>
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
                                <p>Date in ISO format: <strong>{{ date }}</strong></p>
                            </v-flex>
                        </v-layout>
                        <v-layout align-center justify-center row>
                            <v-flex xs1 class="mb-6">
                                <v-btn class="primary">Create planner</v-btn>
                            </v-flex>
                        </v-layout>
                    </v-form>
                </v-flex>
            </v-layout>
        </v-container>
   </v-app>
</template>

<script>
export default {
    data() {
        return {
            topic: '',
            imageURL: '',
            date: null,
            dateFormatted: null,
            menu: false,
            picker: null,
            landscape: false,
        }
    },
    computed: {
        formIsValid () {
            return this.topic !== '' &&
            this.imageURL !== ''
        },
        computedDateFormatted () {
            return this.formatDate(this.date)
        }
    },
    watch: {
      date (val) {
        this.dateFormatted = this.formatDate(this.date)
      }
    },

    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${month}/${day}/${year}`
      },
      parseDate (date) {
        if (!date) return null

        const [month, day, year] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      }
    }
}
</script>


<style lang="stylus">
</style>
