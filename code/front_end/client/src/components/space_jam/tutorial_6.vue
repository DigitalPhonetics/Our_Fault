<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h2>Button Array Module</h2><br>

            <h3>Features of the Button Array Module Module</h3>
            <ul>
                <li>Like the previous modules, the buttons in the button array module come in the following colors (shown below): <b>Green, Blue, </b>and <b>Amber</b></li>
                <li>When describing a buttons's location, they are numbered from the top left corner, that is: the first button in the first column is the top left button.</li>
                <li><b>"First button" refers to the top button in a column, "last button" refers to the bottom button in a column</b></li>
                <li>Solving button array module is done in stages. Each stage starts with a button activated. If you correctly activate a button, you will move to the next
                    stage.</li>
                <li>Some stages may require you to remember which button you pushed in an earlier stage</li>
                <li>In the case of mistakes, you will be imediately notified and the button array will be reset to the start of stage 1</li>
            </ul><br>

            <h3>Try it out:</h3>
            <b>In this example your partner has told you:
                <ul>
                    <li>In the first stage: activate the last button which is in the third column and has the same color as the active button</li>
                    <li>In the second stage: activate the first button in the first column</li>
                    <li>In the third stage: activate the last green button in the second column</li>
                    <li>In the fourth stage: activate the same button that you did in the first stage</li>
                </ul> </b>
            <br><br>
            <svg
             id = "dial_exmaple"
             viewBox="0 0 1366 400">

                <g
                id="g15" transform="translate(-25,-40)">
                <rect
                x="29"
                y="45"
                width="300"
                height="350"
                id="ship_console_background" />
                </g>                

                <!-- Button Array -->

                <g id="memory_column_0" transform="translate(-450,-20)">
                
                <path @click="toggleButton"
                v-bind:class="[memory_0_0_selected ? 'st27' : 'st1']"
                d="M534,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,162.1,534,155.1,534,146.5z"
                id="memory_0_0" />

                <path @click="toggleButton"
                v-bind:class="[memory_0_1_selected ? 'st27' : 'st1']"
                d="M534,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,207.1,534,200.1,534,191.5z"
                id="memory_0_1" />
            
                <path @click="toggleButton"
                v-bind:class="[memory_0_2_selected ? 'st26' : 'st2']"
                d="M534,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,255.1,534,248.1,534,239.5z"
                id="memory_0_2" />

                <path @click="toggleButton"
                v-bind:class="[memory_0_3_selected ? 'st3' : 'st0']"
                d="M534,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C541,303.1,534,296.1,534,287.5z"
                id="memory_0_3" />
                </g>    

                <g id="memory_column_1" transform="translate(-450,-20)">

                <path @click="toggleButton"
                v-bind:class="[memory_1_0_selected ? 'st26' : 'st2']"
                d="M578,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,162.1,578,155.1,578,146.5z"
                id="memory_1_0" />

                <path @click="toggleButton"
                v-bind:class="[memory_1_1_selected ? 'st3' : 'st0']"
                d="M578,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,207.1,578,200.1,578,191.5z"
                id="memory_1_1" />

                <path @click="toggleButton"
                v-bind:class="[memory_1_2_selected ? 'st26' : 'st2']"
                d="M578,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,255.1,578,248.1,578,239.5z"
                id="memory_1_2" />

                <path @click="toggleButton"
                v-bind:class="[memory_1_3_selected ? 'st27' : 'st1']"
                d="M578,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C585,303.1,578,296.1,578,287.5z"
                id="memory_1_3" />
                </g>

                <g id="memory_column_2" transform="translate(-450,-20)">
                <path @click="toggleButton"
                v-bind:class="[memory_2_0_selected ? 'st27' : 'st1']"
                d="M621,146.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,162.1,621,155.1,621,146.5z"
                id="memory_2_0" />

                <path @click="toggleButton"
                v-bind:class="[memory_2_1_selected ? 'st26' : 'st2']"
                d="M621,191.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,207.1,621,200.1,621,191.5z"
                id="memory_2_1" />

                <path @click="toggleButton"
                v-bind:class="[memory_2_2_selected ? 'st3' : 'st0']"
                d="M621,239.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,255.1,621,248.1,621,239.5z"
                id="memory_2_2" />

                <path @click="toggleButton"
                v-bind:class="[memory_2_3_selected ? 'st3' : 'st0']"
                d="M621,287.5c0-8.6,7-15.6,15.6-15.6h0.7c8.6,0,15.6,7,15.6,15.6s-7,15.6-15.6,15.6h-0.7   C628,303.1,621,296.1,621,287.5z"
                id="memory_2_3" />
                </g> 

                <!-- Button Array Indicator -->
                <g
                id="memory_indicator_group"
                transform="matrix(1.0798142,0,0,1,-498.528288,-10)">
                <path
                v-bind:class="[memory_complete ? 'st11' : 'st5']"
                d="M 658.7,76.9 H 537.5 c -1.9,0 -3.5,-3.6 -3.5,-8.1 v 0 c 0,-4.4 1.6,-8.1 3.5,-8.1 h 121.1 c 1.9,0 3.5,3.6 3.5,8.1 v 0 c 0.1,4.4 -1.5,8.1 -3.4,8.1 z"
                id="memory_indicator" />
                <text v-show="memory_complete"
                transform="matrix(1 0 0 1 535 74.4341)"
                class="st22 st13 st21"
                id="memory_indicator_text">Module Complete</text>
                </g>
            </svg>
            
        <div id = "navigation_buttons">
            <div id = "next_button" v-show="memory_complete">
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
    name: 'Tutorial_5',
    data(){ return {
        // button array
        memory_0_0_selected: false,
        memory_0_1_selected: false,
        memory_0_2_selected: false,
        memory_0_3_selected: true,
        memory_1_0_selected: false,
        memory_1_1_selected: false,
        memory_1_2_selected: false,
        memory_1_3_selected: false,
        memory_2_0_selected: false,
        memory_2_1_selected: false,
        memory_2_2_selected: false,
        memory_2_3_selected: false,
        memory_complete: false,
        current_round: 1,
        game_state: "active",
        }
    },
    methods:{
        next_page(){
            this.$parent.tutorial_page += 1;
        },
        previous_page(){
            this.$parent.tutorial_page -=1;
        },
        reset_memory(button){
            setTimeout(() => this._reset(button), 200)

        },
        _reset(button){
            for (let col = 0; col < 3; col++) {
                for (let row = 0; row < 4; row++) {
                this['memory_' + String(col) + '_' + String(row) + "_selected"] = false;
                }
            }
            if (button != "none"){
                this[button] = true;
            }
            this.memory_complete = false;           
        },
        toggleButton(event){
            event.preventDefault();
            if (this.game_state == "active") {
                if (event.target.id.includes("memory")) {
                    for (let col = 0; col < 3; col++) {
                        for (let row = 0; row < 4; row++) {
                        this['memory_' + String(col) + '_' + String(row) + "_selected"] = false;
                        }
                    }        
                }
                var audio = new Audio(require('./sounds/button_sound.wav'));
                audio.play();

                this[event.target.id + '_selected'] = !this[event.target.id + '_selected'];
                if (this.current_round == 1){
                    if (this.memory_2_3_selected){
                        this.reset_memory("memory_1_0_selected");
                        this.current_round = 2;
                    }
                    else{
                        var error_sound = new Audio(require('./sounds/buzzer.wav'));
                        error_sound.play();
                        this.reset_memory("memory_0_3_selected");
                        this.current_round = 1
                    }
                }
                else if (this.current_round == 2){
                    if (this.memory_0_0_selected){
                        this.reset_memory("memory_2_1_selected");
                        this.current_round = 3;
                    }
                    else{
                        var error_sound = new Audio(require('./sounds/buzzer.wav'));
                        error_sound.play();
                        this.reset_memory("memory_0_3_selected");
                        this.current_round = 1
                    }                    
                }
                else if (this.current_round == 3){
                    if (this.memory_1_2_selected){
                        this.reset_memory("memory_2_2_selected");
                        this.current_round = 4;
                    }
                    else{
                        var error_sound = new Audio(require('./sounds/buzzer.wav'));
                        error_sound.play();
                        this.reset_memory("memory_0_3_selected");
                        this.current_round = 1
                    }                    
                }
                else if (this.current_round == 4){
                    if (this.memory_2_3_selected){
                        this.memory_complete = true;
                        var complete_sound = new Audio(require('./sounds/module_complete.wav'));
                        complete_sound.play();                         
                        }
                    else{
                        var error_sound = new Audio(require('./sounds/buzzer.wav'));
                        error_sound.play();
                        this.reset_memory("memory_0_3_selected");
                        this.current_round = 1
                    }                    
                }                                 
            }
        },             
    }    
}

</script>