//use std::process::Command; für den anderen, großen Komentar
use std::io;

fn main() {
    /* Versuchdice.exe zu importieren
    let output = Command::new("dice.exe")
        .output()
        .expect("Failed to execute command");

    println!("Output: {}", output);*/
    
    let mut running = true;
    while running == true {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Fehler beim Lesen der Eingabe");
        //spielbrett
        println!("Astragaloi");
        println!("##########");
        println!("Du hast gewürfelt: <dice>");
        println!("Dein Gegner hat folgende Würfel:");
        println!("   [ -- A -- ] [ -- B -- ] [ -- C -- ]");
        println!(" 3 [ <p2-a3> ] [ <p2-b3> ] [ <p2-c3> ]");
        println!(" 2 [ <p2-a2> ] [ <p2-b2> ] [ <p2-c2> ]");
        println!(" 1 [ <p2-a1> ] [ <p2-b1> ] [ <p2-c1> ]");
        println!("Du hast folgende Würfel:");
        println!("   [ -- A -- ] [ -- B -- ] [ -- C -- ]");
        println!(" 1 [ <p1-a1> ] [ <p1-b1> ] [ <p1-c1> ]");
        println!(" 2 [ <p1-a2> ] [ <p1-b2> ] [ <p1-c2> ]");
        println!(" 3 [ <p1-a3> ] [ <p1-b3> ] [ <p1-c3> ]");
        println!("Wo willst du deinen Würfel platzieren?");
        if input == "x" {
            running = false
        }
    }
}
