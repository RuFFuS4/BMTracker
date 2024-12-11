import animations from '@midudev/tailwindcss-animations';

/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				'primary': '#FF00FF',
				'secondary': '#00FF00',
			},
		},
	},
	plugins: [animations],
}
