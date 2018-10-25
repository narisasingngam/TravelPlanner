<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12 sm10 md8 offset-sm1 offset-md2>
                <v-card class="info">
                    <v-container fluid>
                        <v-layout row>
                            <v-flex xs5 sm4 md3>
                                <v-card-media
                                    src="https://wp-assets.dotproperty-kh.com/wp-content/uploads/sites/14/2016/10/28150318/Fotolia_116473721_Subscription_Monthly_M.jpg"
                                    height="130px"
                                >
                                </v-card-media>
                            </v-flex>
                            <v-flex xs7 sm8 md9>
                                <v-card-title primary-title>
                                    <div>
                                        <h2 class="white--text">My planner</h2>
                                        <div>22 Oct 2018</div>
                                    </div>
                                </v-card-title>
                                <v-card-action>
                                    <v-btn flat to="/planners/1">
                                        <v-icon left light>arrow_forward</v-icon>
                                        View planner</v-btn>
                                </v-card-action>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
