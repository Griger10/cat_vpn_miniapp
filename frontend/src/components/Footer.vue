<script setup>
defineProps({
    botHref: String,
    year: Number,
    uname: String,
});
</script>

<template>
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
</template>
