CREATE MIGRATION m1lfw5in6zp575wyzmawzczblmi5gilrqcgjb5iwzm65vi5gi57dqa
    ONTO m16smqiffrfejvy3augh3t5gv6entzyigx3h46sbvcsmsajdtgc6cq
{
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
      CREATE REQUIRED PROPERTY grade -> default::Grade;
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
      CREATE CONSTRAINT std::max_value(110);
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
