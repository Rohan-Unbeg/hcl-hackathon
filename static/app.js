document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const welcomeState = document.getElementById('welcomeState');
    const resultsContent = document.getElementById('resultsContent');
    const activeFileSection = document.getElementById('activeFileSection');
    const processingIndicator = document.getElementById('processingIndicator');
    const progressBar = document.getElementById('progressBar');
    const statusLabel = document.getElementById('statusLabel');
    const latencyValue = document.getElementById('latencyValue');
    
    const API_KEY = 'sk_track2_987654321';

    // UI Click Handler
    dropZone.addEventListener('click', () => fileInput.click());

    // Drag and Drop
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over');
    });

    ['dragleave', 'dragend'].forEach(type => {
        dropZone.addEventListener(type, () => dropZone.classList.remove('drag-over'));
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over');
        if (e.dataTransfer.files.length) handleFile(e.dataTransfer.files[0]);
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) handleFile(e.target.files[0]);
    });

    async function handleFile(file) {
        const types = {
            'application/pdf': 'pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
            'image/jpeg': 'image', 'image/png': 'image', 'image/jpg': 'image'
        };

        const fileType = types[file.type];
        if (!fileType) return alert('ERR: UNSUPPORTED_FILE_TYPE');

        // Update UI to "Active" state
        document.getElementById('activeFileName').innerText = file.name;
        document.getElementById('activeFileType').innerText = `${fileType.toUpperCase()}_DOCUMENT`;
        activeFileSection.classList.remove('hidden');
        processingIndicator.classList.remove('hidden');
        welcomeState.classList.add('hidden');
        resultsContent.classList.add('hidden');
        updateProgress(20, 'READING_BYTES...');

        const startTime = performance.now();

        try {
            const base64 = await toBase64(file);
            updateProgress(45, 'EXTRACTING_LAYERS...');

            const response = await fetch('/api/document-analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'x-api-key': API_KEY },
                body: JSON.stringify({
                    fileName: file.name,
                    fileType: fileType,
                    fileBase64: base64.split(',')[1] || base64
                })
            });

            if (!response.ok) throw new Error('API_PROCESS_FAILED');

            updateProgress(85, 'SEMANTIC_ANALYSIS...');
            const data = await response.json();
            
            const endTime = performance.now();
            latencyValue.innerText = `${Math.round(endTime - startTime)}ms`;

            updateProgress(100, 'REPORT_GENERATED');
            setTimeout(() => {
                displayResults(data);
                processingIndicator.classList.add('hidden');
            }, 400);

        } catch (error) {
            alert(`ERR: ${error.message}`);
            resetUI();
        }
    }

    function updateProgress(percent, label) {
        progressBar.style.width = `${percent}%`;
        statusLabel.innerText = label;
    }

    function toBase64(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result);
            reader.onerror = reject;
        });
    }

    function displayResults(data) {
        resultsContent.classList.remove('hidden');
        document.getElementById('reportTimestamp').innerText = `TIMESTAMP: ${new Date().toISOString()}`;
        
        const sentimentTag = document.getElementById('sentimentTag');
        sentimentTag.innerText = data.sentiment.toUpperCase();
        sentimentTag.className = `sentiment-tag sentiment-${data.sentiment.toUpperCase()}`;

        document.getElementById('summaryText').innerText = data.summary;

        renderTags('namesList', data.entities.names);
        renderTags('orgsList', data.entities.organizations);
        renderTags('datesList', data.entities.dates);
        renderTags('amountsList', data.entities.amounts);

        document.getElementById('rawJson').innerText = JSON.stringify(data, null, 2);
    }

    function renderTags(id, items) {
        const container = document.getElementById(id);
        container.innerHTML = '';
        if (!items || items.length === 0) {
            container.innerHTML = '<span style="color:var(--text-low)">NULL</span>';
            return;
        }
        items.forEach(item => {
            const span = document.createElement('span');
            span.innerText = item;
            container.appendChild(span);
        });
    }

    function resetUI() {
        activeFileSection.classList.add('hidden');
        welcomeState.classList.remove('hidden');
        resultsContent.classList.add('hidden');
    }
});
