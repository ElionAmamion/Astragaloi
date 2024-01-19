use std::process::Command;

fn main() {

    let output = Command::new("<link>dice.exe</link>")
        .output()
        .expect("Failed to run the executable");

    println!("Output: {:?}", output);

    /*println!("Astragaloi");
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
    println!("Wo willst du deinen Würfel platzieren?");*/
}
