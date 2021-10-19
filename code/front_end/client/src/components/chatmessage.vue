<template>
    <div v-if="party === 'system'" class="speech-bubble-system">
		<div class="message">
			{{ message }}
			<p class="party">System</p>
		</div>
    </div>
    <div v-else-if="party === 'user'" class="speech-bubble-user">
		<div class="message">
			{{ message }}
			<p class="party">User</p>
		</div>
    </div>
</template>

<script>
export default {
    name: 'Chatmessage',
    props: {
        party: String,
        message: String,
    },
};
</script>

<style scoped>
.speech-bubble-system {
	position: relative;
	background: #0061ff;
	border-radius: .4em;
	text-align: left;
	width: auto;
	float: left;
	clear: both;
	margin-bottom: 5px;
	margin-top: 5px;
}

.speech-bubble-system:after {
	content: '';
	position: absolute;
	left: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 21px solid transparent;
	border-right-color: #0061ff;
	border-left: 0;
	border-top: 0;
	margin-top: -10.5px;
	margin-left: -21px;
}

.speech-bubble-user {
	position: relative;
	background: #929292;
	border-radius: .4em;
	text-align: right;
	float: right;
	clear: both;
	margin-top: 5px;
	margin-bottom: 5px;
}

.speech-bubble-user:after {
	content: '';
	position: absolute;
	right: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 21px solid transparent;
	border-left-color: #929292;
	border-right: 0;
	border-top: 0;
	margin-top: -10.5px;
	margin-right: -21px;
}

.message {
	padding: 5px;
	color: white;
}

.party {
	margin-bottom: -1px;
	font-size: x-small;
	font-weight: lighter;
}
</style>