<script lang="ts">
	import api from '../fetch';
	let prompt = '';
	let result = '';
	const keydown = async (e: KeyboardEvent) => {
		if (e.key === 'Enter') {
			const res = await api('/prompt', 'POST', {
				prompt
			});
			result = res.message;
			prompt = '';
		}
	};
</script>

<h1>Python girlfriend</h1>
<p>Type something...</p>
<input type="text" bind:value={prompt} on:keydown={keydown} />
<p>{result}</p>
