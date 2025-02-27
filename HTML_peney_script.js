// Simulation simple : lancer une partie dès que l'utilisateur clique sur "start"
document.getElementById("start").addEventListener("click", async function() {
    // Récupération et validation des séquences entrées par l'utilisateur
    let seq1 = document.getElementById("seq1").value.toUpperCase();
    let seq2 = document.getElementById("seq2").value.toUpperCase();
    
    if (!/^[PF]{3}$/.test(seq1) || !/^[PF]{3}$/.test(seq2)) {
        alert("Les séquences doivent contenir exactement 3 lettres (P ou F).");
        return;
    }
    
    // Réinitialisation des zones d'affichage
    document.getElementById("result").textContent = "";
    document.getElementById("coin-container").innerHTML = "";
    
    let sequence = "";
    let tossCount = 0;
    
    // Boucle de simulation : on continue de lancer jusqu'à obtenir une des séquences souhaitées
    while (true) {
        tossCount++;
        // Lancer de pièce avec animation
        let flipResult = await flipCoinAnimation();
        sequence += flipResult;
        
        // Mise à jour de l'affichage de la séquence en cours
        document.getElementById("result").textContent = `Séquence actuelle : ${sequence}`;
        
        // Vérifier si la séquence se termine par l'une des séquences attendues
        if (sequence.endsWith(seq1)) {
            document.getElementById("result").textContent += `\nGagnant : ${seq1} en ${tossCount} lancers.`;
            saveResult({ winner: seq1, tosses: tossCount });
            break;
        }
        if (sequence.endsWith(seq2)) {
            document.getElementById("result").textContent += `\nGagnant : ${seq2} en ${tossCount} lancers.`;
            saveResult({ winner: seq2, tosses: tossCount });
            break;
        }
    }
});

// Fonction d'animation d'un lancer de pièce
function flipCoinAnimation() {
    return new Promise((resolve) => {
        const coinContainer = document.getElementById("coin-container");
        
        // Créer un élément image pour l'animation du flip (image à fournir : coin_flip.gif)
        let coinImg = document.createElement("img");
        coinImg.src = "coin_flip.gif";
        coinImg.alt = "Lancer de pièce...";
        coinImg.classList.add("coin"); // Possibilité de styler cette image via CSS
        coinContainer.appendChild(coinImg);
        
        // Durée de l'animation (ici 1 seconde)
        const animationDuration = 1000;
        setTimeout(() => {
            // Supprimer l'image d'animation
            coinContainer.removeChild(coinImg);
            
            // Déterminer le résultat du lancer (Pile ou Face)
            const result = Math.random() < 0.5 ? "P" : "F";
            
            // Créer un élément image statique pour afficher le résultat (images à fournir : heads.png et tails.png)
            let resultImg = document.createElement("img");
            resultImg.src = result === "P" ? "heads.png" : "tails.png";
            resultImg.alt = result === "P" ? "Pile" : "Face";
            resultImg.classList.add("coin-result");
            coinContainer.appendChild(resultImg);
            
            // Petite pause avant de résoudre la promesse (pour laisser le temps d'observer le résultat)
            setTimeout(() => {
                resolve(result);
            }, 500);
        }, animationDuration);
    });
}

/* --------------------- BONUS --------------------- */
// Fonction pour sauvegarder le résultat d'une simulation dans le localStorage
function saveResult(result) {
    let history = JSON.parse(localStorage.getItem("penneyHistory")) || [];
    history.push(result);
    localStorage.setItem("penneyHistory", JSON.stringify(history));
    updateHistoryDisplay();
}

// Met à jour l'affichage de l'historique dans l'élément avec l'id "history"
function updateHistoryDisplay() {
    let historyList = document.getElementById("history");
    if (!historyList) return; // Si l'élément n'existe pas, ne rien faire
    let history = JSON.parse(localStorage.getItem("penneyHistory")) || [];
    historyList.innerHTML = "";
    history.forEach((entry, index) => {
        let li = document.createElement("li");
        li.textContent = `Simulation ${index + 1} : Gagnant ${entry.winner}, lancers : ${entry.tosses}`;
        historyList.appendChild(li);
    });
}

// Bouton bonus : Réinitialiser l'historique des simulations
document.getElementById("resetHistory").addEventListener("click", function() {
    localStorage.removeItem("penneyHistory");
    updateHistoryDisplay();
});

// Bouton bonus : Lancer plusieurs simulations automatiquement
document.getElementById("simulateMultiple").addEventListener("click", async function() {
    let rounds = parseInt(prompt("Nombre de simulations à exécuter :", "10"));
    if (isNaN(rounds) || rounds <= 0) {
        alert("Veuillez entrer un nombre valide de simulations.");
        return;
    }
    
    let seq1 = document.getElementById("seq1").value.toUpperCase();
    let seq2 = document.getElementById("seq2").value.toUpperCase();
    if (!/^[PF]{3}$/.test(seq1) || !/^[PF]{3}$/.test(seq2)) {
        alert("Les séquences doivent contenir exactement 3 lettres (P ou F).");
        return;
    }
    
    // Réinitialiser l'historique pour cette série de simulations
    localStorage.removeItem("penneyHistory");
    updateHistoryDisplay();
    
    // Boucle pour exécuter plusieurs simulations
    for (let i = 0; i < rounds; i++) {
        document.getElementById("coin-container").innerHTML = "";
        document.getElementById("result").textContent = `Simulation ${i + 1} en cours...`;
        let sequence = "";
        let tossCount = 0;
        while (true) {
            tossCount++;
            let flipResult = await flipCoinAnimation();
            sequence += flipResult;
            document.getElementById("result").textContent = `Simulation ${i + 1} : Séquence actuelle : ${sequence}`;
            if (sequence.endsWith(seq1)) {
                document.getElementById("result").textContent += `\nGagnant : ${seq1} en ${tossCount} lancers.`;
                saveResult({ winner: seq1, tosses: tossCount });
                break;
            }
            if (sequence.endsWith(seq2)) {
                document.getElementById("result").textContent += `\nGagnant : ${seq2} en ${tossCount} lancers.`;
                saveResult({ winner: seq2, tosses: tossCount });
                break;
            }
        }
        // Pause d'une seconde entre chaque simulation pour la lisibilité
        await new Promise(r => setTimeout(r, 1000));
    }
});

// Afficher l'historique au chargement de la page (si déjà présent)
updateHistoryDisplay();
