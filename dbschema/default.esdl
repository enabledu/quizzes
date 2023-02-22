module default {
    type User {
        required property first_name -> str;
        required property last_name -> str;
        required property username -> str {
            constraint exclusive;
        }
        required property age -> Age;
        multi link quizzes -> Quiz;
    }
    
    type Question {
        required property title -> str;
        required property content -> str;
        required multi link choices -> Choice;
        required property grades -> Grade;
    }

    type Choice {
        required property content -> str;
        required property is_correct -> bool{default := false};
    }

    type Quiz {
        required property title -> str;
        required multi link questions -> Question;
        property is_login_required -> bool{default := false};
    }
    
    scalar type Grade extending int16{
        constraint max_value(100);
        constraint min_value(0);
    }

    scalar type Age extending int16{
        constraint max_value(120);
        constraint min_value(0);
    }
}


