# ROADMAP PENYELESAIAN PROJECT — Kelompok 4

## A. Screenshot yang WAJIB diambil

### Deployment (1x saja)
- [ ] Cockpit → Dashboard → semua process definitions terdaftar
- [ ] Cockpit → Decisions → DMN terdaftar (Decision_TierKlasifikasi)
- [ ] Admin → Users → daftar 5 user aktif
- [ ] Admin → Groups → daftar 5 group

### Per Proses — minimal 3 skenario masing-masing

#### P1: Penentuan Pengampu MK
Skenario 1A (Normal): adaViolation=false, semua approve
- [ ] Start form terisi
- [ ] Tasklist novikps: task "Korprodi Input" muncul
- [ ] Tasklist adrezo: task "Dosen Konfirmasi" muncul
- [ ] Tasklist erlywadek: task "Wadek Approve" muncul
- [ ] Discord: notifikasi SIAKAD tersinkron
- [ ] Cockpit: instance COMPLETED + variabel akhir

Skenario 1B (Violation): adaViolation=true
- [ ] Discord: notifikasi Flag Violation
- [ ] Tasklist novikps: task "Korprodi Revisi" muncul
- [ ] Cockpit: instance melewati violation path

Skenario 1C (Dosen Tolak): isDosenSetuju=false
- [ ] Tasklist novikps: task "Assign Dosen Pengganti" muncul
- [ ] Cockpit: retryAssignDosen variable visible

#### P2: Pemilihan Pembimbing TA
Skenario 2A (Normal): isKHSValid=true, isApprovedPembimbing=true
- [ ] Start form terisi (nama, NIM, SKS, dosen)
- [ ] Tasklist adrezo: task "PA Validasi" muncul
- [ ] Tasklist vegamhs: task "Browse Marketplace" + "Submit Request"
- [ ] Tasklist adrezo: task "Pembimbing Review"
- [ ] Discord: notifikasi konfirmasi semua pihak
- [ ] Cockpit: instance COMPLETED

Skenario 2B (PA Tolak): isKHSValid=false
- [ ] Discord: notifikasi penolakan ke mahasiswa (improvement baru!)
- [ ] Cockpit: instance COMPLETED via rejection path

Skenario 2C (Pembimbing Reject): isApprovedPembimbing=false
- [ ] Tasklist vegamhs: "Cari Pembimbing Lain" muncul
- [ ] Cockpit: retryPembimbing variable visible

#### P3: Pemantauan Masa Studi
Skenario 3A (Tier 1): semesterAktif=10
- [ ] Cockpit: BRT output tier=1
- [ ] Discord: notifikasi Tier 1 ke PA
- [ ] Tasklist adrezo: task PA Review muncul

Skenario 3B (Tier 3): semesterAktif=14
- [ ] Cockpit: BRT output tier=3
- [ ] Discord: eskalasi Dekanat
- [ ] Tasklist novikps: task Intervensi muncul

Skenario 3C (Tier 0): semesterAktif=6
- [ ] Cockpit: BRT output tier=0
- [ ] Instance COMPLETED tanpa intervensi

#### P4: Pembuatan RPS
Skenario 4A (Normal): semua level approve
- [ ] Start form terisi (MK, dosen koordinator)
- [ ] Subprocess "Penyusunan Draft RPS" visible di Cockpit
- [ ] Tasklist adrezo: task "Dosen Input" + "Dosen Submit"
- [ ] Tasklist novikps: task "L1 Korprodi Review"
- [ ] Tasklist gkm4: task "L2 GKM Review"
- [ ] Tasklist erlywadek: task "L3 Wadek Approve"
- [ ] Discord: notifikasi Publish RPS
- [ ] Cockpit: instance COMPLETED

Skenario 4B (L1 Reject): isL1Approved=false
- [ ] Tasklist novikps: catatan revisi terisi
- [ ] Tasklist adrezo: task "Dosen Revisi" muncul dengan catatan L1

Skenario 4C (L2 Reject): isL2Approved=false
- [ ] Tasklist gkm4: catatan GKM terisi
- [ ] Tasklist adrezo: task "Dosen Revisi" muncul dengan catatan L2

### Monitoring Aggregat
- [ ] Cockpit Dashboard: ringkasan instance running/completed
- [ ] Cockpit per process: instance count
- [ ] Cockpit Decisions: decision instance result untuk P3

---

## B. Hal yang perlu dilengkapi di Laporan

### Update yang diperlukan:
1. **Abstrak** — update jumlah form (24 file), DMN (aktif 1 di P3, 3 lainnya sebagai desain)
2. **BAB 5.5** — tambahkan tabel semua 24 form files (P1: 7, P2: 7, P3: sesuai, P4: 10)
3. **BAB 5.6** — sudah ada 4 DMN, tapi jelaskan hanya P3 yang di-link BRT
4. **BAB 6.2** — tambahkan penjelasan subprocess di P4 dan BRT di P3
5. **BAB 6.3** — jelaskan migrasi dari embedded formData ke external formRef
6. **BAB 6.5** — sisipkan screenshot deployment
7. **BAB 6.6** — isi 12 skenario pengujian (3 per proses) dengan data aktual
8. **BAB 7.1** — isi tabel monitoring dari screenshot Cockpit
9. **BAB 7.2** — tulis analisis berdasarkan hasil simulasi nyata
10. **BAB 7.3** — isi evaluasi KPI dengan data aktual
11. **BAB 8** — tambahkan improvement yang sudah diimplementasikan (P2: notif penolakan, re-check kuota, retry counter, jalur eskalasi tercatat)
12. **Lampiran** — sisipkan semua screenshot

### Yang sudah bagus dan tidak perlu diubah:
- BAB 1-4 (Pendahuluan, Studi Kasus, Discovery, Analysis)
- BAB 5.1-5.4 (Prinsip, BPMN To-Be, Alur, Task list)
- BAB 9 (Kesimpulan — update minor saja)

---

## C. Deliverables lain yang masih perlu
- [ ] Slide presentasi (8-12 slide)
- [ ] Video demonstrasi (7-12 menit)
- [ ] Repository (GitHub/Google Drive) dengan struktur folder sesuai ketentuan
