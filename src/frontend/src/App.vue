<script setup>
import {ref, computed, onMounted} from 'vue'
import {request} from './js/api.js'
import {init, initData, viewport} from '@telegram-apps/sdk'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

init()
viewport.mount()
initData.restore()
viewport.expand()

const CONFIG = {botUsername: '@kitten_vpn_bot'}

const vpnKey = ref('Не указано')
const vpnKeyExpiry = ref(null) // дата истечения ключа или null
const showHelp = ref(false)
const showToast = ref(false)
const toastMessage = ref('')

const year = computed(() => new Date().getFullYear())
const uname = computed(() => CONFIG.botUsername)
const unameClean = computed(() =>
    uname.value.startsWith('@') ? uname.value.slice(1) : uname.value
)
const botHref = computed(() => `https://t.me/${unameClean.value}`)

const vpnKeyExpiryText = computed(() => {
    if (!vpnKeyExpiry.value) return 'Бессрочный'

    return vpnKeyExpiry.value
})

const openHelp = () => (showHelp.value = true)
const closeHelp = () => (showHelp.value = false)

function triggerToast(message) {
    toastMessage.value = message
    showToast.value = true
    setTimeout(() => (showToast.value = false), 1700)
}

async function copyKey() {
    try {
        await navigator.clipboard.writeText(vpnKey.value)
        triggerToast('Ключ скопирован')
    } catch {
        const ta = document.createElement('textarea')
        ta.value = vpnKey.value
        ta.setAttribute('readonly', '')
        ta.style.position = 'absolute'
        ta.style.left = '-9999px'
        document.body.appendChild(ta)
        ta.select()
        document.body.removeChild(ta)
        triggerToast('Ключ скопирован')
    }
}

onMounted(async () => {
    const {data} = await request('users/info/')
    if (data.vpn_key) vpnKey.value = data.vpn_key
    if (data.vpn_key_expiry) vpnKeyExpiry.value = data.vpn_key_expiry
})
</script>

<template>
    <div class="min-h-screen bg-gray-950 text-gray-100 antialiased selection:bg-brand-600/30">
        <div class="min-h-screen flex flex-col">
            <Header/>
            <main class="flex-1">
                <div class="max-w-3xl mx-auto px-4 sm:px-6 py-8">
                    <section class="bg-white/5 border border-white/10 rounded-2xl shadow-xl shadow-black/30 p-4 sm:p-6">
                        <div class="grid gap-4 sm:grid-cols-[1fr_auto] sm:items-end">
                            <div class="min-w-0">
                                <p class="text-sm text-white/60 mb-1">Ваш ключ доступа</p>
                                <input
                                    class="block w-full bg-black/40 border border-white/10 rounded-xl px-3 sm:px-4 py-3 font-mono text-xs sm:text-sm tracking-wider focus:outline-none focus:ring-2 focus:ring-brand-600/50 overflow-x-auto"
                                    :value="vpnKey"
                                    readonly
                                />
                                <p class="mt-1 text-xs text-white/50">Действителен до: {{ vpnKeyExpiryText }}</p>
                            </div>

                            <div class="flex flex-col sm:flex-row gap-3 sm:gap-2">
                                <button
                                    class="w-full sm:w-auto px-4 py-3 rounded-xl bg-brand-600/90 hover:bg-brand-700 transition text-gray-50 text-sm font-medium shadow-lg"
                                    @click="copyKey"
                                >
                                    Скопировать ключ
                                </button>
                                <button
                                    class="w-full sm:w-auto px-4 py-3 rounded-xl border border-white/15 bg-white/5 hover:bg-white/10 transition text-sm font-medium"
                                    @click="openHelp"
                                >
                                    Смотреть инструкцию
                                </button>
                            </div>
                        </div>
                    </section>
                </div>
            </main>
            <Footer :bot-href="botHref" :uname="uname" :year="year"/>

            <transition name="fade">
                <div v-if="showHelp" class="fixed inset-0 z-50 flex items-center justify-center p-4">
                    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" @click.self="closeHelp"></div>
                    <div
                        class="relative w-full max-w-lg max-h-[90vh] overflow-y-auto bg-gray-900 border border-white/10 rounded-2xl p-6 shadow-2xl">
                        <div class="flex items-start justify-between gap-4">
                            <h2 class="text-lg font-semibold">Инструкция по подключению</h2>
                            <button class="p-2 -m-2 text-white/70 hover:text-white" @click="closeHelp">✕</button>
                        </div>
                        <ol class="mt-4 space-y-3 text-sm text-white/80 list-decimal list-inside">
                            <li>Установите приложение-клиент (WireGuard, Outline, ShadowSocks).</li>
                            <li>Скопируйте ключ и вставьте в приложение.</li>
                            <li>Сохраните профиль и подключитесь.</li>
                            <li>Если возникнут вопросы, напишите в бота {{ uname }}.</li>
                        </ol>
                    </div>
                </div>
            </transition>

            <transition name="fade">
                <div v-if="showToast" class="fixed bottom-4 inset-x-0 flex justify-center z-50">
                    <div class="px-4 py-2 rounded-lg bg-black/80 border border-white/10 text-sm">{{
                            toastMessage
                        }}
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.15s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

