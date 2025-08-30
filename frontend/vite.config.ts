import path from 'node:path'
import {defineConfig, loadEnv} from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig(({mode}) => {
    const rootDir = "./"

    loadEnv(mode, rootDir, '')

    const isDev = mode === 'development'

    return {
        rootDir,

        plugins: [
            vue(),
            ...(isDev ? [vueDevTools()] : []),
            tailwindcss(),
        ],

        resolve: {
            alias: {
                '@': path.resolve(rootDir, 'src'),
            },
        },

        esbuild: isDev
            ? {}
            : {
                drop: ['console', 'debugger'],
            },

        build: {
            sourcemap: false,
            minify: 'esbuild',
            target: 'esnext',
        },
    }
})
