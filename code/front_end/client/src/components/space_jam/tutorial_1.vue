<template>
    <fragment>
        <div id = "wrapper">
            <br><br>
            <h1> Hello There Welcome to Space Jam!</h1>
            <br>
            <!-- It looks like you've gotten yourself into a bit of trouble! <br><br>

            All you wanted to do was take your shiny new space cruiser out for a test run, but now
            your being attacked by space pirates! And the worst thing is, in your rush to try out your new ship, you didn't configure the onboard AI, so you have
            no idea how to activate your warp drive engine to get out of there. Luckily if you can describe your control panel well enough, the AI should be able
            to help you figure out what you need to do before your shield gives out. <br><br> -->

            <h2>What is Space Jam?</h2>
            Space Jam is a two player cooperative puzzle game. You will be playing the role of the hapless space pilot who forgot to configure his ship's AI and your
            partner (a computer) will play the role of the AI system. As the pilot, you will be shown a control panel made of four puzzle modules, but
            you will have no instructions to solve them. Your partner will be given an instruction manual, but will not be able to see the exact configuration of
            puzzle elements. You will need to work together to solve all four puzzle modules before time runs out. <br><br>

            <br>

            <h2>Data Collection Policy</h2>
            Please consider this information carefully before deciding whether to accept this task.
            <br><br>
            <b>TITLE OF RESEARCH:</b> Investigation of human and non-human explanations in the context of a cooperative online game.
            <br><br>
            <b>PURPOSE OF RESEARCH:</b> To examine different kinds of explanations for effectively modelling the behavior of an AI dialogue-agent.
            <br><br>
            <b>WHAT YOU WILL DO:</b> You will take part in the study summarized above, interacting via text with a human or AI partner to solve a series of four puzzles and 
            then answer a questionnaire about the experience.
            <br><br>
            <b>TIME REQUIRED:</b> Participation will take approximately 30 minutes.
            <br><br>
            <b>RISKS:</b> There are no anticipated risks associated with participating in this study. The effects of participating should be comparable to those you would 
            experience from viewing a computer monitor for 30 minutes and using a mouse and keyboard.
            <br><br>
            <b>LIMITATIONS:</b> This task is unsuitable for color-blind participants.
            <br><br>
            <b>CONFIDENTIALITY:</b> Your participation in this study will remain confidential. Your responses will be assigned a code number. You will NOT be asked to provide 
            your name. You will be asked to provide your age and gender. Throughout the experiment, we may collect data such as your textual input, and your feedback in 
            form of a questionnaire. The records of this study will be kept private. In any sort of report we make public we will not include any information that will 
            make it possible to identify you without your explicit consent. Research records will be kept in a locked file; only the researchers will have access to the 
            records.
            <br><br>
            <b>PARTICIPATION AND WITHDRAWAL:</b> Your participation in this study is voluntarily, and you may withdraw at any time.
            <br><br>
            <b>DATA REGULATION:</b> Your data will be processed for the following purposes:
            <ul>
                <li>Analysis of the respondents' evaluations of the cooperative online game, the dialogue system and the explanations given by the system</li>
                <li>Analysis of potential influencing factors for individual behavior of the participants in the interaction with the dialog system</li>
                <li>Scientific publication based on the results of the above analyses</li>
            </ul>
            Your data will be processed on the basis of Article 6 paragraph 1 subparagraph 1 letter a GDPR. Data, which is related to your person, will be deleted by 
            30.06.2021 at the latest.
            You are entitled to the following rights (for details see  <a href="https://www.uni-augsburg.de/de/impressum/datenschutz/#ix-rechte-der-betroffenen-person6393">here</a>)
            <ul>
                <li>You have the right to receive information about the data stored about your person.</li>
                <li>Should incorrect personal data be processed, you have the right to correct it.</li>
                <li>Under certain conditions, you can demand the deletion or restriction of the processing as well as object to the processing.</li>
                <li>In general, you have a right to data transferability.</li>
                <li>Furthermore, you have the right of appeal to the Bavarian State Commissioner for Data Protection.</li>
            </ul>
            You can revoke your consent for the future at any time. The legality of the data processing carried out on the basis of the consent until revocation is not 
            affected by this.
            <br><br>
            RISKS: There are no anticipated risks associated with participating in this study. The effects of participating should be comparable to those you would experience from viewing a computer monitor for 30 minutes and using a mouse.
            <br><br>
            COMPENSATION: Upon completion of this task, you will receive a code to enter on the Amazon Mechanical Turk task page.
            <br><br>
            <b>CONTACT:</b> This study is conducted by researchers at the University of Stuttgart and the University of Augsburg. If you have any questions or concerns about 
            this study, please contact Katharina Weitz katharina.weitz@informatik.uni-augsburg.de or Lindsey Vanderlyn, vanderly@ims.uni-stuttgart.de
            <br><br>
            The responsible data protection officer is Prof. Dr. Ulrich M. Gassner, University of Augsburg, Universitätsstraße 24, 86159 Augsburg, 
            e-mail: datenschutzbeauftragter@uni-augsburg.de, Tel. 0821/598-4600.            


            <br><br>

        <div id = "navigation_buttons">
            <div id = "next_button">
                <b-button
                    variant="success"
                    @click="next_page">
                    Agree and Continue
                </b-button>              
            </div>
        </div>
        <br><br>
    </div>


    </fragment>
</template>

<style scoped>

#next_button {
    float: right;
}

#wrapper{
    width: 80%;
    margin: auto;
}

</style>

<script>
import { mapState } from "vuex";

export default {
    name: 'Tutorial_1',
    computed: {
      
      ...mapState(["token"]),
    },
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/ws?token=" + this.token);
        this.socket.onopen = (event) => {
          //this.startDialog();
        };
      };
    },    
    methods:{
        has_token: function() {
            return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
        },        
        next_page(){
            this.$parent.tutorial_page += 1;
        if (this.has_token()){
            this.socket.send(JSON.stringify({
                topic: "user_consented",
                access_token: this.token,
            }));
          };
        },
    },
}

</script>