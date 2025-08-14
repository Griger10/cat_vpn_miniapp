<script setup>
import {ref, computed, onMounted} from 'vue'
import {request} from "./js/api.js";

const CONFIG = {
    botUsername: '@kitten_vpn_bot'
}

const vpnKey = ref('Не указано')
const showHelp = ref(false)
const showToast = ref(false)
const toastMessage = ref('')

const year = computed(() => new Date().getFullYear())
const uname = computed(() => CONFIG.botUsername)
const unameClean = computed(() => (uname.value.startsWith('@') ? uname.value.slice(1) : uname.value))
const botHref = computed(() => `https://t.me/${unameClean.value}`)

function openHelp() {
    showHelp.value = true
}

function closeHelp() {
    showHelp.value = false
}

function triggerToast(message) {
    toastMessage.value = message
    showToast.value = true
    setTimeout(() => {
        showToast.value = false
    }, 1700)
}

async function copyKey() {
    try {
        await navigator.clipboard.writeText(vpnKey.value)
        triggerToast('Ключ скопирован')
    } catch (e) {
        try {
            const ta = document.createElement('textarea')
            ta.value = vpnKey.value
            ta.setAttribute('readonly', '')
            ta.style.position = 'absolute'
            ta.style.left = '-9999px'
            document.body.appendChild(ta)
            ta.select()
            document.body.removeChild(ta)
            triggerToast('Ключ скопирован')
        } catch {
            triggerToast('Скопируйте ключ вручную')
        }
    }
}

onMounted(async () => {
    let data = await request(
        'users/info/',
    ).data
    if (data.vpnKey) {
        vpnKey.value = data.vpnKey
    }
})

</script>

<template>
    <div class="min-h-screen bg-gray-950 text-gray-100 antialiased selection:bg-brand-600/30">
        <div class="min-h-screen flex flex-col">
            <header class="border-b border-white/5 bg-gradient-to-b from-white/5 to-transparent">
                <div class="max-w-3xl mx-auto px-4 sm:px-6 py-5 flex items-center justify-between">
                    <h1 class="text-xl sm:text-2xl font-semibold tracking-tight flex items-center gap-2">
                        <span class="text-2xl">🐾</span>
                        <span>Кот VPN</span>
                    </h1>
                </div>
            </header>

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
                                    aria-label="VPN ключ"
                                />
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

                    <div class="mt-6 grid gap-4 sm:grid-cols-2">
                        <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                            <div class="text-sm text-white/70">Подсказка</div>
                            <div class="text-xs text-white/50 mt-1">
                                Ключ храните в надёжном месте. Никому его не передавайте.
                            </div>
                        </div>
                        <div class="rounded-xl border border-white/10 bg-white/5 p-4">
                            <div class="text-sm text-white/70">Совместимость</div>
                            <div class="text-xs text-white/50 mt-1">
                                Работает с популярными клиентами WireGuard/Outline/ShadowSocks (пример). Адаптируйте под
                                ваш стек.
                            </div>
                        </div>
                    </div>
                </div>
            </main>

            <footer class="mt-auto border-t border-white/5">
                <div
                    class="max-w-3xl mx-auto px-4 sm:px-6 py-6 flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-0 sm:justify-between">
                    <div class="text-xs text-white/50">© {{ year }} Кот VPN</div>
                    <a :href="botHref" target="_blank" rel="noopener"
                       class="text-sm text-brand-500 hover:text-brand-600 underline underline-offset-4 break-all">
                        Бот: <span>{{ uname }}</span>
                    </a>
                </div>
            </footer>

            <transition name="fade">
                <div
                    v-if="showHelp"
                    class="fixed inset-0 z-50 items-center justify-center p-4 flex"
                    @keydown.esc="closeHelp"
                >
                    <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" @click.self="closeHelp"></div>
                    <div
                        class="relative w-full max-w-lg max-h-[90vh] overflow-y-auto bg-gray-900 border border-white/10 rounded-2xl p-6 shadow-2xl">
                        <div class="flex items-start justify-between gap-4">
                            <h2 class="text-lg font-semibold">Инструкция по подключению</h2>
                            <button class="p-2 -m-2 text-white/70 hover:text-white" @click="closeHelp">✕</button>
                        </div>
                        <ol class="mt-4 space-y-3 text-sm text-white/80 list-decimal list-inside">
                            <li>Установите приложение-клиент (WireGuard, Outline, ShadowSocks — используйте нужный вам
                                вариант).
                            </li>
                            <li>Нажмите «Скопировать ключ» и вставьте ключ в нужное поле приложения.</li>
                            <li>Сохраните профиль и подключитесь к серверу.</li>
                            <li>Готово! Если возникли вопросы, напишите в нашего бота <span>{{ uname }}</span>.</li>
                        </ol>
                        <div class="mt-6 flex items-center justify-end gap-3">
                            <button
                                class="px-4 py-2 rounded-lg border border-white/15 bg-white/5 hover:bg-white/10 text-sm"
                                @click="closeHelp">
                                Понятно
                            </button>
                        </div>
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
* {
    scrollbar-width: thin;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity .15s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
