CREATE MIGRATION m1qwnbfeg75qbjz45zphbp36jxq62ilfd72ylulqekatd6ytjm7d2q
    ONTO initial
{
  CREATE FUTURE nonrecursive_access_policies;
  CREATE TYPE default::Choice {
      CREATE REQUIRED PROPERTY content -> std::str;
      CREATE REQUIRED PROPERTY is_correct -> std::bool {
          SET default := false;
      };
  };
  CREATE SCALAR TYPE default::Grade EXTENDING std::int16 {
      CREATE CONSTRAINT std::max_value(100);
      CREATE CONSTRAINT std::min_value(0);
  };
  CREATE TYPE default::Question {
      CREATE REQUIRED MULTI LINK choices -> default::Choice;
      CREATE REQUIRED PROPERTY content -> std::str;
      CREATE REQUIRED PROPERTY grades -> default::Grade;
      CREATE REQUIRED PROPERTY title -> std::str;
  };
  CREATE TYPE default::Quiz {
      CREATE REQUIRED MULTI LINK questions -> default::Question;
      CREATE PROPERTY is_login_required -> std::bool {
          SET default := false;
      };
      CREATE REQUIRED PROPERTY title -> std::str;
  };
  CREATE SCALAR TYPE default::Age EXTENDING std::int16 {
      CREATE CONSTRAINT std::max_value(120);
      CREATE CONSTRAINT std::min_value(0);
  };
  CREATE TYPE default::User {
      CREATE MULTI LINK quizzes -> default::Quiz;
      CREATE REQUIRED PROPERTY age -> default::Age;
      CREATE REQUIRED PROPERTY first_name -> std::str;
      CREATE REQUIRED PROPERTY last_name -> std::str;
      CREATE REQUIRED PROPERTY username -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
