const CONFIG = {
    vpnKey: 'XXXX-XXXX-XXXX-XXXX',
    botUsername: '@cat_vpn_bot'
};

const keyInput = document.getElementById('vpnKeyInput');
const copyBtn = document.getElementById('copyKeyBtn');
const helpBtn = document.getElementById('helpBtn');
const yearEl = document.getElementById('year');
const botLink = document.getElementById('botLink');
const botUsernameText = document.getElementById('botUsernameText');
const botUsernameInline = document.getElementById('botUsernameInline');
const helpModal = document.getElementById('helpModal');
const toastEl = document.getElementById('toast');
const toastMsg = document.getElementById('toastMsg');

function init() {
    const uname = CONFIG.botUsername;
    const unameClean = uname.startsWith('@') ? uname.slice(1) : uname;

    keyInput.value = CONFIG.vpnKey;
    yearEl.textContent = new Date().getFullYear();
    botUsernameText.textContent = uname;
    botUsernameInline.textContent = uname;
    botLink.href = `https://t.me/${unameClean}`;
}

function toast(message) {
    toastMsg.textContent = message;
    toastEl.classList.remove('hidden');
    setTimeout(() => {
        toastEl.classList.add('hidden');
    }, 1700);
}

async function copyKey() {
    try {
        await navigator.clipboard.writeText(keyInput.value);
        toast('Ключ скопирован');
    } catch (e) {
        keyInput.removeAttribute('readonly');
        keyInput.select();
        keyInput.setAttribute('readonly', '');
        toast('Ключ скопирован');
    }
}

function openHelp() {
    helpModal.classList.remove('hidden');
    helpModal.classList.add('flex');
}

function closeHelp() {
    helpModal.classList.add('hidden');
    helpModal.classList.remove('flex');
}

copyBtn.addEventListener('click', copyKey);
helpBtn.addEventListener('click', openHelp);
helpModal.addEventListener('click', (e) => {
    if (e.target.hasAttribute('data-close')) closeHelp();
});

init();