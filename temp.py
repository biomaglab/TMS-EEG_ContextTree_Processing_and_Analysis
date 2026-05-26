import mne

caminho = r"C:\Pessoais\Victor Moraes\TMS-EEG_ContextTree_Processing_and_Analysis\data\raw\V06_data\V06_data.bdf"

# 1. Carrega
raw = mne.io.read_raw_bdf(caminho, preload=True)

# 2. Atualiza as anotações
raw.set_annotations(raw.annotations[raw.annotations.description != "8Bit 8"])

# 3. Salva de volta em BDF usando a função de exportação
# O parâmetro fmt='bdf' garante que o MNE converta corretamente
mne.export.export_raw(caminho, raw, fmt="bdf", overwrite=True)

print("Arquivo BDF atualizado e salvo com sucesso!")