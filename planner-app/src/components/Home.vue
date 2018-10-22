<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs12 sm6 class="text-xs-center text-sm-right">
                <v-btn large router to="/planners" class="primary">Explore Planners</v-btn>
            </v-flex>
            <v-flex xs12 sm6 class="text-xs-center text-sm-right">
                <v-btn large router to="/planner/new" class="primary">Organize Planners</v-btn>
            </v-flex>
        </v-layout>
        <v-layout row wrap>
           <v-carousel>
                <v-carousel-item
                v-for="planner in planners"
                :key="planner.id"
                :src="planner.imageUrl"
                ></v-carousel-item>
                </v-carousel>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    data () {
        return {
            planners: [
                { imageUrl: 'https://wp-assets.dotproperty-kh.com/wp-content/uploads/sites/14/2016/10/28150318/Fotolia_116473721_Subscription_Monthly_M.jpg', 
                id: '213', title:"Planner in Bangkok"},
                { imageUrl: 'https://www.viagemegastronomia.com.br/wp-content/uploads/2015/12/chiang-mai.jpg', 
                id: '1234', title:"Planner in Chiang mai"},
            ]
        }
    }
}
</script>
