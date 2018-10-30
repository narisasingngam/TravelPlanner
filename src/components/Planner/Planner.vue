<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12x>
                <v-card>
                    <v-card-title>
                        <h1 class="primary--text">My planner</h1>
                    </v-card-title>
                    <v-card-media
                                src="https://wp-assets.dotproperty-kh.com/wp-content/uploads/sites/14/2016/10/28150318/Fotolia_116473721_Subscription_Monthly_M.jpg"
                                height="400px"
                    ></v-card-media>
                    <v-card-text>
                        <div class="info--text">22 Oct 2018</div>
                    </v-card-text>
                    <v-form>
                        <v-layout align-center justify-center row>
                            <v-flex xs2 >
                                <v-text-field
                                name="place"
                                label="Place"
                                id="place"
                                v-model="place"
                                required></v-text-field>
                            </v-flex>
                            <v-flex xs2 >
                                <v-text-field
                                name="time"
                                label="Time"
                                id="time"
                                v-model="time"
                                required></v-text-field>
                            </v-flex>
                            <v-flex xs2>
                                <v-text-field
                                name="duration"
                                label="Duration"
                                id="duration"
                                v-model="duration"
                                required></v-text-field>
                            </v-flex>
                        </v-layout>
                    </v-form>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn 
                        class="primary"
                        @click="addPlace"
                        >Add place</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout row>
            <v-flex xs12>
                <v-data-table
                    :headers="headers"
                    :items="list"
                    hide-actions
                    class="elevation-1"
                >
                    <template slot="items" slot-scope="props">
                        <td>{{ props.item.time }}</td>
                        <td class="text-xs-right">{{ props.item.name }}</td>
                        <td class="text-xs-right">{{ props.item.timeDuration }}</td>
                    </template>
                </v-data-table>
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
        headers: [
          {
            text: 'Time',
            align: 'left',
            sortable: false,
            value: 'time',
          },
          { text: 'Places', value: 'name', },
          { text: 'Duration', value: 'timeDuration', },
        ],
        list: [
          
        ],
      }
    },
    methods: {
        addPlace() {
            this.list.push({
                time: this.time,
                name: this.place,
                timeDuration: this.duration,
                completed: false,
            })
            this.timeDuration = ''
        },
    },
}
</script>

