<template>
    <div>
        <div v-show="tutorial_page == 1">
        <tutorial_1/>
        </div>

        <div v-show="tutorial_page == 2">
        <tutorial_2/>
        </div>

        <div v-show="tutorial_page == 3">
        <tutorial_3/>
        </div>

        <div v-show="tutorial_page == 4">
        <tutorial_4/>
        </div>

        <div v-show="tutorial_page == 5">
        <tutorial_5/>
        </div>

        <div v-show="tutorial_page == 6">
        <tutorial_6/>
        </div>

        <div v-show="tutorial_page == 7">
        <tutorial_7/>
        </div>                              
    </div>
</template>

<script>

import Tutorial_1 from './tutorial_1.vue';
import Tutorial_2 from './tutorial_2.vue';
import Tutorial_3 from './tutorial_3.vue';
import Tutorial_4 from './tutorial_4.vue';
import Tutorial_5 from './tutorial_5.vue';
import Tutorial_6 from './tutorial_6.vue';
import Tutorial_7 from './tutorial_7.vue';

export default {
    name: 'Tutorial',
    components: {
        tutorial_1: Tutorial_1,
        tutorial_2: Tutorial_2,
        tutorial_3: Tutorial_3,
        tutorial_4: Tutorial_4,
        tutorial_5: Tutorial_5,
        tutorial_6: Tutorial_6,
        tutorial_7: Tutorial_7,
    },
    data() {
      return {
          tutorial_page: 1
      }
    }    
}
</script>

<style>

</style>