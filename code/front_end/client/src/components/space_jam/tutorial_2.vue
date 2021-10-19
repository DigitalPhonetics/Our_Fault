<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2> How to Play</h2><br>

            <h3>Communicating with Your Partner</h3>
            <ul>
                <li><b>Communicating with your partner is NECESSARY to win the game</b></li>
                <li>ALL communication will take place through a text interface.</li>
                <li>To save on memory, only the most recent message from you and your partner will be displayed.</li>
                <li><b>YOUR PARTNER WILL NOT BE ABLE TO SEE OR HEAR THE CONTROL PANEL INTERFACE, SO MAKE SURE TO INFORM THEM ABOUT THE FOLLOWING:</b></li>
                <ul>
                    <li><b>When you complete an action OR something doesn't work</b></li>
                    <li><b>If your partner makes a MISTAKE</b></li>
                    <li><b>What the curren puzzle looks like</b></li>
                </ul>
                <li>Once you start a puzzle, you can only reset it if you make a mistake</li>
            </ul>

            <h3>Winning and Losing the Game</h3> 
            <b>Winning:</b> If you solve all four puzzle modules, you win!<br>

            <b>Losing:</b> The game is timed and if the <b>time/shield power runs out</b>, you lose <br><br>

            <h3>Completing Modules</h3>
            <ul>
                <li>Module chime will sound</li>
                <li>Indicator light will turn on above the module</li>
                <li>Warp drive power will increase</li>
                <li><b>Must completed in order proposed by your partner</b></li>
            </ul>

            <h3>Penalties for Mistakes</h3>
            <ul>
                <li>The buzzer will sound</li>
                <li><b>Time will be subtracted</b></li>
                <li>The <b>module will be reset</b>.</li>
            </ul>

            <h3>Computer Sound</h3>
            For the best experience, make sure that the sound is on!          
            <br><br><br>
        <div id = "navigation_buttons">
            <div id = "next_button">
                <b-button
                    variant="success"
                    @click="next_page">
                    Next
                </b-button>             </div>
            <div id = "back_button">
                <b-button
                    variant="danger"
                    @click="previous_page">
                    Back
                </b-button>             </div>
        </div>
        </div>


    </fragment>
</template>

<style scoped>

#next_button {
    float: right;
}

#back_button{
    float: left;
}

#wrapper{
    width: 80%;
    margin: auto;
}

</style>

<script>
export default {
    name: 'Tutorial_2',
    methods:{
        next_page(){
            this.$parent.tutorial_page += 1;
        },
        previous_page(){
            this.$parent.tutorial_page -= 1;
        }        
    }    
}

</script>